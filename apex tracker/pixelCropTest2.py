from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import cv2
import pyautogui
import tkinter as tk
from tkinter import filedialog
import time
import PIL
import numpy
from PIL import Image
from pytesseract import pytesseract
import math
import re
  
f = open("coordinates.txt", "a")
while True:
  
    time.sleep(1)


    img = pyautogui.screenshot()

        
    left = 48
    top = 60
    right = 190
    bottom = 72
     
      
    img = img.crop((left, top, right, bottom)) 
    img.save("imageTest.png")

    output = ""
    i = -7
    while i < 120:
        
        i = i + 8
        j = i+9
        img_mod = img.crop((i, 0, j, 12))
        img_mod.save("images\cropTest" + str(i) + ".png")
        
        #img_mod = cv2.imread("images\cropTest" + str(i) + ".png")
        #img_mod = cv2.cvtColor(img_mod, cv2.COLOR_BGR2GRAY)

        #print("i is: " + str(i))
        im = Image.open("images/cropTest" + str(i) + ".png")
        #im = Image.open("images/cropTest9.png")
        #im = Image.open("zoneImages/2.png")
        pix = im.load()
        #print (im.size)  # Get the width and hight of the image for iterating over

        '''
        value = (255, 0, 0, 255)
        pix[3,4] = value  
        pix[2,3] = value  
        pix[2,9] = value  
        pix[7,3] = value  
        pix[7,9] = value  
        pix[6,8] = value  
        im.save('alive_parrot.png')  # Save the modified pixels as .png
        '''
          
        def isPixelWhite(e):
            sum = 0
            for i in e:
                sum = sum + i
            res = sum / len(e)

            if res > 200:
                #print("pixel is white")
                return True
            else:
                #print("non-white pixel")
                return False

        def isPixelDark(e):
            sum = 0
            for i in e:
                sum = sum + i
            res = sum / len(e)

            if res < 200:
                #print("non-white pixel")
                return True    
            else:
               # print("pixel is white")
                return False
                


        def isPixelZero():
            value = 0
            
            value = value + isPixelWhite((pix[3, 4]))  
            value = value + isPixelWhite((pix[2, 3]))  
            value = value + isPixelWhite((pix[2, 9]))  
            value = value + isPixelWhite((pix[7, 3]))  
            value = value + isPixelWhite((pix[7, 9]))  
            value = value + isPixelWhite((pix[6, 8])) 
            if (value == 6):
                return True
            else: return False

        def isPixelOne():
            value = 0
            
            value = value + isPixelWhite((pix[3, 10]))  
            value = value + isPixelWhite((pix[3, 2]))  
            value = value + isPixelWhite((pix[4, 4]))  
            value = value + isPixelWhite((pix[6, 10]))  
         
           
            if (value == 4):
                return True
            else: return False

        def isPixelTwo():
            value = 0
            
            value = value + isPixelWhite((pix[2, 3]))  
            value = value + isPixelWhite((pix[2, 9]))  
            #value = value + isPixelWhite((pix[2, 7]))  
            value = value + isPixelWhite((pix[5, 6]))  
            value = value + isPixelWhite((pix[5, 10]))  
         
            
            if (value == 4):
                return True
            else: return False
            
        def isPixelThree():
            value = 0
            
            value = value + isPixelWhite((pix[2, 3]))  
            value = value + isPixelWhite((pix[2, 9]))  
            value = value + isPixelWhite((pix[4, 6]))  
            value = value + isPixelWhite((pix[6, 10]))  
            value = value + isPixelWhite((pix[7, 4]))  
            value = value + isPixelDark((pix[2, 6]))  
         
            
            if (value == 6):
                return True
            else: return False
            
        def isPixelFour():
            value = 0
            
            value = value + isPixelWhite((pix[2, 2]))  
            value = value + isPixelWhite((pix[3, 6]))  
            value = value + isPixelWhite((pix[7, 2]))  
            value = value + isPixelWhite((pix[7, 10]))   
         
            
            if (value == 4):
                return True
            else: return False
            
        def isPixelFive():
            value = 0
            
            value = value + isPixelWhite((pix[4, 2]))  
            value = value + isPixelWhite((pix[2, 9]))  
            value = value + isPixelWhite((pix[3, 5]))  
            value = value + isPixelWhite((pix[7, 8]))  
            value = value + isPixelDark((pix[2, 7]))  
            value = value + isPixelDark((pix[7, 4]))  
         
            
            if (value == 6):
                return True
            else: return False
            
        def isPixelSix():
            value = 0
            
            value = value + isPixelWhite((pix[2, 5]))  
            value = value + isPixelWhite((pix[2, 7]))  
            value = value + isPixelWhite((pix[6, 2]))  
            value = value + isPixelWhite((pix[6, 10]))  
            value = value + isPixelDark((pix[7, 4]))  
         
            
            if (value == 5):
                return True
            else: return False
            
        def isPixelSeven():
            value = 0
            
            value = value + isPixelWhite((pix[2, 2]))  
            value = value + isPixelWhite((pix[2, 10]))  
            value = value + isPixelWhite((pix[5, 5]))  
            value = value + isPixelWhite((pix[7, 2]))  
         
            
            if (value == 4):
                return True
            else: return False
            
        def isPixelEight():
            value = 0
            
            value = value + isPixelWhite((pix[2, 3]))  
            value = value + isPixelWhite((pix[2, 7]))  
            value = value + isPixelWhite((pix[3, 6]))  
            value = value + isPixelWhite((pix[4, 10]))  
            value = value + isPixelWhite((pix[5, 2]))  
            value = value + isPixelWhite((pix[5, 6]))  
            value = value + isPixelWhite((pix[7, 3]))  
            value = value + isPixelWhite((pix[7, 7]))  
         
            
            if (value == 8):
                return True
            else: return False
            
        def isPixelNine():
            value = 0
            
            value = value + isPixelWhite((pix[2, 3]))  
            value = value + isPixelDark((pix[2, 7]))  
            value = value + isPixelWhite((pix[3, 6]))  
            value = value + isPixelWhite((pix[4, 10]))  
            value = value + isPixelWhite((pix[5, 2]))  
            value = value + isPixelWhite((pix[5, 6]))  
            value = value + isPixelWhite((pix[7, 3]))  
            value = value + isPixelWhite((pix[7, 7]))  
         
            
            if (value == 8):
                return True
            else: return False
            
        def isPixelNegative():
            value = 0
            
            value = value + isPixelWhite((pix[3, 6]))      
            value = value + isPixelWhite((pix[4, 6]))  
            value = value + isPixelWhite((pix[5, 6]))  
         
            
            if (value == 3):
                return True
            else: return False

        def checkNumbers():
            if isPixelZero():
                return 0
            elif isPixelOne():
                return 1
            elif isPixelThree():
                return 3
            elif isPixelFour():
                return 4
            elif isPixelFive():
                return 5
            elif isPixelSix():
                return 6
            elif isPixelSeven():
                return 7
            elif isPixelEight():
                return 8
            elif isPixelNine():
                return 9
            elif isPixelTwo():
                return 2
            elif isPixelNegative():
                return "Negative"
          

        '''
        value = (255, 0, 0, 255)
        pix[4, 9] = value  
        pix[4, 10] = value  
        pix[5, 9] = value  
        pix[5, 10] = value  
        value = (0, 255, 0, 255)
        pix[3, 8] = value  
        pix[3, 11] = value  
        pix[6, 8] = value  
        pix[6, 11] = value 
        im.save('alive_parrot.png')  # Save the modified pixels as .png
        '''


        result = checkNumbers()

        output = output + str(result)


    output = output.replace("Negative", "-")
    output = output.replace("\n", "")

    output = output.replace("None", ".")
    output = output.replace(".-", " -")
    output = re.sub("\\.\\d\\d\\.", " ", output)
    print(output)
    f.write(output + str("\n"))
f.close()