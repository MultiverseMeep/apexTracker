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
from datetime import datetime
  
#who the fuck designed datetime so that it gives a formtat that can't be used as a filename/????? /?? isn't HTat ltiearlly the whole point????
Currenttime = datetime.today()
Currenttime = str(Currenttime)
Currenttime = Currenttime.replace(" ", "_")
Currenttime = Currenttime.replace(":", "-")
Currenttime = re.sub("\\.\\d\\d\\d\\d\\d", "", Currenttime)
f = open("coordinateData/" + str(Currenttime) + str(".csv"), "a")
while True:
   
    time.sleep(1)
    
    #take screenshot, and then shred it to bits (crop it properly)
    img = pyautogui.screenshot()
    left = 48
    top = 60
    right = 190
    bottom = 72  
    img = img.crop((left, top, right, bottom)) 

    #because python is fucking stupid and can't figure out what i meant if i don't make this an empty string first
    output = ""
    
    
    i = -7
    while i < 120:
        
        i = i + 8
        j = i+9
        img_mod = img.crop((i, 0, j, 12))
        
        #what the fuckis this stupidity?? just put it as a variable dumbass
        img_mod.save("images\cropTest" + str(i) + ".png")
        im = Image.open("images/cropTest" + str(i) + ".png")
   
        pix = im.load()
    
        #i want to apologise to everybody who is about to read this bullshit below this comment, because this is honestly the most horrnedous fucking code i have ever written. I am sorry.     
      
        #this function is like a cop. White = good, dark = bad
        def isPixelWhite(e):
            sum = 0
            for i in e:
                sum = sum + i
            res = sum / len(e)
            if res > 200:             
                return True
            else: return False

        #backwwards cop??                                          wit no brim
        def isPixelDark(e):
            sum = 0
            for i in e:
                sum = sum + i
            res = sum / len(e)
            if res < 200:
                return True    
            else: return False             

        #tesseract is too fucking stupid to tell the difference between an 8 and a 3 at 9*12 pixels, so I had to do thsi bullshit
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
            #this was as painful to write as it was to look at. I need mental help           
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
            #i had to put two at the end, because sevne is the fuckls[aing worst number on the dgoddamn plannet it is like 4am when i figuerd this out i am wanting to not alive
            elif isPixelTwo():
                return 2
            elif isPixelNegative():
                return "Negative"
         
        result = checkNumbers()
        output = output + str(result)

    output = output.replace("Negative", "-")
    output = output.replace("\n", "")
    output = output.replace("None", ".")
    output = output.replace(".-", " -")
    #had to ask for help on this because regex on python is actually dumb
    output = re.sub("\\.\\d\\d\\.", " ", output)
    f.write(output + str("\n"))
f.close()