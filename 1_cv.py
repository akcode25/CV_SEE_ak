
#1. Create 2D img using OpenCV for diff objs

import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(image, (50, 50), (200, 150), (255, 0, 0), -1)
cv2.circle(image, (300, 100), 50, (0, 255, 0), -1)
cv2.line(image, (100, 300), (300, 300), (0, 0, 255), 2)

cv2.imshow("2D Objects Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()