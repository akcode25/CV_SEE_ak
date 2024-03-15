
#1. Create 2D img using OpenCV for diff objs

import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(image, (50, 50), (200, 150), (193, 182, 255), -1)
cv2.circle(image, (300, 100), 50, (255, 255, 255), -1)
cv2.line(image, (100, 300), (300, 300), (19, 69, 139), 2)


cv2.circle(image, (0, 0), 7, (0, 0, 255), -1)
cv2.circle(image, (0, 500), 7, (0, 255, 0), -1)
cv2.circle(image, (500, 0), 7, (255, 0, 0), -1)
cv2.circle(image, (500, 500), 7, (255, 255, 255), -1)


cv2.imshow("2D Objects Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
