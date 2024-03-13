
# 7. Draw a triangle with centroid using OpenCV, change its color using mouse/keyboard interface.

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



