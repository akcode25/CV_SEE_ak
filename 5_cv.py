
# 5. Erosion and Dilation of images using OpenCV in python.

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


# erosion(less) to slide a structuring element (also known as a kernel or mask) over the image. 
# At each position of the kernel..
# IF ALL the pixels underneath the kernel - white, then, remains - white. else, becomes black.

# dilation(more), expands the boundaries of foreground objects in an image.
# IF ATLEAST ONE pixel under the kernel - white, then, pixel being considered becomes white. Otherwise, it remains black.


