
# 9. Creation and representation a 3D scene with movements  using OpenCV

import cv2
import numpy as np
import math

def draw_sky(img):
    sky_color = (250, 206, 135)  
    cv2.rectangle(img, (0, 0), (800, 600), sky_color, -1)  #topleft, bottomright, -1(filled) (+:outlinethinkness)

def draw_garden(img):
    grass_color = (0, 128, 0)  
    cv2.rectangle(img, (0, 350), (800, 600), grass_color, -1)

def draw_sun(img, angle):
    sun_color = (0, 255, 255)  

    # Calculate sun position based on the angle
    sun_x = int(700 * math.cos(angle) + 100)
    sun_y = int(100 * math.sin(angle) + 100)
    cv2.circle(img, (sun_x, sun_y), 40, sun_color, -1)

def draw_car(img, x, y):
    car_color = (0, 0, 0) 
    wheel_color = (0, 0, 0)  

    cv2.rectangle(img, (x, y), (x + 60, y + 30), car_color, -1)
    # windows
    cv2.rectangle(img, (x + 10, y + 5), (x + 20, y + 15), (255, 255, 255), -1)
    cv2.rectangle(img, (x + 30, y + 5), (x + 40, y + 15), (255, 255, 255), -1)
    cv2.circle(img, (x + 10, y + 30), 5, wheel_color, -1)  # Front wheel
    cv2.circle(img, (x + 50, y + 30), 5, wheel_color, -1)  # Rear wheel

def draw_house(img):
    house_color = (193, 182, 255)  # Pink 
    window_color = (255, 255, 255)  # White 
    door_color = (19, 69, 139)  # Brown

    # house structure in one corner
    cv2.rectangle(img, (50, 150), (230, 370), house_color, -1)
    #  windows
    cv2.rectangle(img, (90, 190), (130, 230), window_color, -1)
    cv2.rectangle(img, (90, 270), (130, 310), window_color, -1)
    cv2.rectangle(img, (170, 190), (210, 230), window_color, -1)
    cv2.rectangle(img, (170, 270), (210, 310), window_color, -1)
    # door
    cv2.rectangle(img, (130, 330), (170, 370), door_color, -1)

def draw_mountain(img):
    mountain_color = (0, 63, 123)  
    points = np.array([[600, 350], [800, 50], [800, 350]]) # triangular shape
    cv2.drawContours(img, [points], 0, mountain_color, -1) # triangle

def draw_car2(img, x, y):
    car_color = (43, 43, 210)  # Redish 
    wheel_color = (0, 0, 0)  

    cv2.rectangle(img, (x, y), (x + 60, y + 30), car_color, -1)
    # windows
    cv2.rectangle(img, (x + 10, y + 5), (x + 20, y + 15), (255, 255, 255), -1)
    cv2.rectangle(img, (x + 30, y + 5), (x + 40, y + 15), (255, 255, 255), -1)
    cv2.circle(img, (x + 10, y + 30), 5, wheel_color, -1)  # Front wheel
    cv2.circle(img, (x + 50, y + 30), 5, wheel_color, -1)  # Rear wheel


# Initialize OpenCV window
cv2.namedWindow('My 3D Scene', cv2.WINDOW_NORMAL)
cv2.resizeWindow('My 3D Scene', 800, 600) #resizable window named 'My 3D Scene' with dimensions 800x600 pixels 

sun_angle = 0
car_x = 200  # Initial x-coordinate for the car

while True:
    # sky blue background
    img = np.zeros((600, 800, 3), dtype=np.uint8)  #3 rgb channels #8 bit int 0-255 #pixel intencity
    draw_sky(img)
    draw_garden(img) 
    draw_sun(img, sun_angle) 
    draw_house(img)
    draw_car(img, car_x, 450)  
    draw_mountain(img)  
    draw_car2(img, 750 - car_x * 2, 500)
    
    cv2.imshow('My 3D Scene', img)
    
    sun_angle += 0.005 
    car_x += 1 

    key = cv2.waitKey(30)
    if key == ord('q'):  # ESC key to exit
      break

cv2.destroyAllWindows() #closes the OpenCV window and releases resources.

