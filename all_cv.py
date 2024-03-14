
#1.

import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(image, (50, 50), (200, 150), (255, 0, 0), -1)
cv2.circle(image, (300, 100), 50, (0, 255, 0), -1)
cv2.line(image, (100, 300), (300, 300), (0, 0, 255), 2)

cv2.imshow("2D Objects Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#2.

import cv2
import numpy as np
import math

cube_size = 100
cube_color = (255, 255, 255)
cube_thickness = 2

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

angle = 0 

while True:
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 1, 1]], dtype=np.float32)
        
    rotated_vertices = np.dot(vertices, rotation_matrix)

    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([300, 300])).astype(int)

    frame = np.ones((600, 600, 3), dtype=np.uint8) #* background_color

    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    cv2.imshow("Rotating 3D Cube", frame.astype(np.uint8))
    key = cv2.waitKey(30)
    if key == ord('q'): break
    angle += 0.03
        
cv2.destroyAllWindows()


#3.

import cv2
import numpy as np
import math

def on_size_change(value):
    global circle_radius, cube_size
    circle_radius = cube_size = value

img_2d = np.zeros((500, 500, 3), dtype=np.uint8) 

circle_center = (300, 300)
circle_color = cube_color = (255, 255, 255)

cube_size = 100
cube_thickness = 2

angle = 0

cv2.namedWindow("Resizable 2D and 3D Images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resizable 2D and 3D Images", 500, 500)
cv2.createTrackbar("Size", "Resizable 2D and 3D Images", cube_size, 100, on_size_change)

while True:
    #2d
    img_2d = np.zeros((500, 500, 3), dtype=np.uint8)
    cv2.circle(img_2d, circle_center, circle_radius, circle_color, -1)
    cv2.imshow("Resized 2D img", img_2d)
    #3d
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
    
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 1, 1]], dtype=np.float32)

    rotated_vertices = np.dot(vertices, rotation_matrix)

    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([300, 300])).astype(int)

    frame = np.zeros((500, 500, 3), dtype=np.uint8) #black

    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    cv2.imshow("Resizable 3D Image", frame)

    key = cv2.waitKey(30)
    if key == ord('q'): break
    angle += 0.03

cv2.destroyAllWindows()


#4. 

import cv2
import numpy as np
import math

cube_size = 100
cube_color = (255, 255, 255)
cube_thickness = 2

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

angle = 0 
while True:
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 0, 1]], dtype=np.float32)     # [0,1,1] # 2D rotation - no transformation along the z-axis
    
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Project the 3D points to 2D
    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([300, 300])).astype(int)

    frame = np.ones((500, 500, 3), dtype=np.uint8) #* background_color

    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]]) # Get starting point coordinates
        pt2 = tuple(projected_vertices[edge[1]]) # Get ending point coordinates
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    cv2.imshow("Rotating 2D Square", frame.astype(np.uint8))
    key = cv2.waitKey(30)
    if key == ord('q'): break
    angle += 0.03

cv2.destroyAllWindows()


#5.

import cv2
import numpy as np

img = cv2.imread('C:/Users/aka-pc/Downloads/pic.jpg', 0)  #0 =>cv2.IMREAD_GRAYSCALE
kernel = np.ones((5,5), np.uint8)

eroded_image = cv2.erode(img,kernel,1) #iterations=1
dilated_image = cv2.dilate(img,kernel,1)

cv2.imshow('Origianl Image', img)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#6.

import cv2
import numpy as np

image = cv2.imread('C:/Users/aka-pc/Downloads/pic.jpg')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

cv2.imshow('Original Image', image)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#7.

import cv2
import numpy as np

img = np.zeros((500,500,3), np.uint8)
color = (255,255,255)
vertices = np.array([[250,100], [100,400], [400,400]])

while True:
    cv2.fillPoly(img, [vertices.reshape(-1,1,2)], color)
    
    centroid = np.mean(vertices, axis=0, dtype=np.uint32)    
    cv2.circle(img, centroid, 5, (0,0,0), -1)
    cv2.imshow("centroid", img)

    key = cv2.waitKey(0)
    if key == ord('c'):
        color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
    if key == ord('q'): break

cv2.destroyAllWindows()


#8.

import cv2
import numpy as np
import math

cube_size = 100
cube_thickness = 2

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

colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
         (0, 255, 255), (255, 0, 255), (255, 255, 0)]

angle_x, angle_y, angle_z = 0, 0, 0 # for rotation matrix

while True:
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, math.cos(angle_x), -math.sin(angle_x)],
                                  [0, math.sin(angle_x), math.cos(angle_x)]], dtype=np.float32)

    rotation_matrix_y = np.array([[math.cos(angle_y), 0, -math.sin(angle_y)],
                                  [0, 1, 0],
                                  [math.sin(angle_y), 0, math.cos(angle_y)]], dtype=np.float32)

    rotation_matrix_z = np.array([[math.cos(angle_z), -math.sin(angle_z), 0],
                                  [math.sin(angle_z), math.cos(angle_z), 0],
                                  [0, 0, 1]], dtype=np.float32)

    rotated_vertices = np.dot(vertices, rotation_matrix_x)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_y)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_z)

    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([300, 300])).astype(int)

    image = np.zeros((500, 500, 3), dtype=np.uint8)     # Create a black image (cover dhabbe)

    # Draw cube faces
    for i, face in enumerate([(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
                              (2, 6, 7, 3), (1, 2, 6, 5), (0, 3, 7, 4)]):

        pts = projected_vertices[face, :]
        cv2.fillPoly(image, [pts], color=colors[i])

    # Draw cube edges
    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(image, pt1, pt2, (255, 255, 255), cube_thickness)

    cv2.imshow("Rotating 3D Cube", image)
    key = cv2.waitKey(30)
    if key == ord('q'): break

    angle_x += 0.03
    angle_y += 0.03
    angle_z += 0.03

cv2.destroyAllWindows()

