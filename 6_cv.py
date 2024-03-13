
# 6. Convert an image from one color space to another.

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
