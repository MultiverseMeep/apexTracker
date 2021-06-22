# Python program to take
# screenshots
  
  
import numpy as np
import cv2
import pyautogui
import cv2
import time
  
time.sleep(2)
# take screenshot using pyautogui
image = pyautogui.screenshot()
   
# since the pyautogui takes as a 
# PIL(pillow) and in RGB we need to 
# convert it to numpy array and BGR 
# so we can write it to the disk
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
   
# writing it to the disk using opencv


image = cv2.imread('image1.png')
y=0
x=100
h=200
w=200
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
cv2.waitKey(0) 
cv2.imwrite("image1.png", image)
