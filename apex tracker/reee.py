import pyautogui
import tkinter as tk
from tkinter import filedialog
import time
import PIL
import cv2
import numpy
from PIL import Image
from pytesseract import pytesseract
  

#while True:

time.sleep(1)


img = pyautogui.screenshot()

    
left = 40
top = 60
right = 310
bottom = 72
 
  
img = img.crop((left, top, right, bottom)) 
img.save("imageTest.png")
 
i = 0
while i < 270:
    i = i + 1
    j = i+9
    img_mod = img.crop((i, 0, j, 12))
    img_mod.save("images\cropTest" + str(i) + ".png")
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#pil_image = PIL.Image.open('imageTest.png').convert('RGB') 
#open_cv_image = numpy.array(pil_image) 
# Convert RGB to BGR 
#open_cv_image = open_cv_image[:, :, ::-1].copy() 


#open_cv_image.show() 
#open_cv_image.save("imageTest.png")

#  img_grey = cv2.imread("imageTest.png", cv2.IMREAD_GRAYSCALE)

# define a threshold, 128 is the middle of black and white in grey scale
# thresh = 128

# threshold the image
#  img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

#save image
#cv2.imwrite("black-and-white.png",img_binary) 







# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = "imageTest.png"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])