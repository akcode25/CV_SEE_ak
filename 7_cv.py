
# 7. Draw a triangle with centroid using OpenCV, change its color using mouse/keyboard interface.

import cv2
import numpy as np

# unsigned 8-bit integer => each element in array can have values 0 to 255
image = np.zeros((500, 500, 3), dtype=np.uint8) # Create a black image 

vertices = np.array([[250, 50], [50, 450], [450, 450]], dtype=np.int32)

cv2.polylines(image, [vertices], isClosed=True, color=(0, 255, 0), thickness=2) # Draw the triangle

centroid = np.mean(vertices, axis=0, dtype=np.int32)
cv2.circle(image, tuple(centroid), radius=5, color=(255, 255, 255), thickness=-1) #centroid-small circle

cv2.imshow("Triangle with Centroid", image) # Display the image
cv2.waitKey(0)

def change_color(event, x, y, flags, param):
    global image
    if event == cv2.EVENT_LBUTTONDOWN:
        new_color = np.random.randint(0, 256, size=3).tolist()
        cv2.polylines(image, [vertices], isClosed=True, color=new_color, thickness=2)
        cv2.imshow("Triangle with Centroid", image)

cv2.setMouseCallback("Triangle with Centroid", change_color) #function call change_color

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
