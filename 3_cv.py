
# 3. 2D  and 3D image resizing OpenGL/OpenCV for different objects

import cv2
import numpy as np
import math

def on_size_change(value):
    global circle_radius, cube_size
    circle_radius = value
    cube_size = value

img_2d = np.zeros((500, 500, 3), dtype=np.uint8)  #300x300 black screen

#2d parameters
circle_center = (150, 150)
circle_color = (255, 255, 255)
#3d parameters
cube_size = 100
cube_color = (255, 255, 255)
cube_thickness = 2

angle = 0

cv2.namedWindow("Resizable 2D and 3D Images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resizable 2D and 3D Images", 500, 500)
cv2.createTrackbar("Size", "Resizable 2D and 3D Images", cube_size, 100, on_size_change)

while True:

    # Resize 2D Image (Circle)
    img_2d = np.zeros((500, 500, 3), dtype=np.uint8)
    cv2.circle(img_2d, circle_center, circle_radius, circle_color, -1)
    cv2.imshow("Resized 2D img", img_2d)

    vertices = np.array([[-1, -1, -1],
                         [1, -1, -1],
                         [1, 1, -1],
                         [-1, 1, -1],
                         [-1, -1, 1],
                         [1, -1, 1],
                         [1, 1, 1],
                         [-1, 1, 1]], dtype=np.float32)
    
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]
    
    scaled_vertices = vertices * (cube_size / 100)

    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 1, 1]], dtype=np.float32)

    rotated_vertices = np.dot(scaled_vertices, rotation_matrix)

    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([300, 300])).astype(int)

    frame = np.zeros((500, 500, 3), dtype=np.uint8) #black

    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    cv2.imshow("Resizable 3D Image", frame)

    key = cv2.waitKey(30)
    if key == ord('q'):
        break

    angle += 0.02

cv2.destroyAllWindows()
