# import the necessary packages
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
  

 
 
 
 
 
 

f = open("coords.txt", "a")

#while True:
#    try:
def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = numpy.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()
    
    # load the images -- the original, the original + library,
# and the original + photoshop
original = cv2.imread("imageTest.png")
library0 = cv2.imread("numberLibrary/0.png")
library1 = cv2.imread("numberLibrary/1.png")
library2 = cv2.imread("numberLibrary/2.png")
library3 = cv2.imread("numberLibrary/3.png")
library4 = cv2.imread("numberLibrary/4.png")
library5 = cv2.imread("numberLibrary/5.png")
library6 = cv2.imread("numberLibrary/6.png")
library7 = cv2.imread("numberLibrary/7.png")
library8 = cv2.imread("numberLibrary/8.png")
library9 = cv2.imread("numberLibrary/9.png")

libraryPeriod = cv2.imread("numberLibrary/period.png")
libraryNegative = cv2.imread("numberLibrary/negative.png")
libraryPixel = cv2.imread("numberLibrary/pixel.png")
#shopped = cv2.imread("black-and-white.png")
# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
library0 = cv2.cvtColor(library0, cv2.COLOR_BGR2GRAY)
library1 = cv2.cvtColor(library1, cv2.COLOR_BGR2GRAY)
library2 = cv2.cvtColor(library2, cv2.COLOR_BGR2GRAY)
library3 = cv2.cvtColor(library3, cv2.COLOR_BGR2GRAY)
library4 = cv2.cvtColor(library4, cv2.COLOR_BGR2GRAY)
library5 = cv2.cvtColor(library5, cv2.COLOR_BGR2GRAY)
library6 = cv2.cvtColor(library6, cv2.COLOR_BGR2GRAY)
library7 = cv2.cvtColor(library7, cv2.COLOR_BGR2GRAY)
library8 = cv2.cvtColor(library8, cv2.COLOR_BGR2GRAY)
library9 = cv2.cvtColor(library9, cv2.COLOR_BGR2GRAY)

libraryPeriod = cv2.cvtColor(libraryPeriod, cv2.COLOR_BGR2GRAY)
libraryNegative = cv2.cvtColor(libraryNegative, cv2.COLOR_BGR2GRAY)
libraryPixel = cv2.cvtColor(libraryPixel, cv2.COLOR_BGR2GRAY)
#shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("library0", library0), ("library1", library1), ("library2", library2), ("library3", library3), ("library4", library4), ("library5", library5), ("library6", library6), ("library7", library7), ("library8", library8), ("library9", library9), ("libraryPeriod", libraryPeriod), ("libraryNegative", libraryNegative), ("libraryPixel", libraryNegative)
# loop over the images
#for (i, (name, image)) in enumerate(images):
    # show the image
#	ax = fig.add_subplot(1, 3, i + 1)
#	ax.set_title(name)
    #plt.imshow(image, cmap = plt.cm.gray)
    #plt.axis("off")
# show the figure

# compare the images
#compare_images(original, original, "Original vs. Original")



#while True:

time.sleep(1)


img = pyautogui.screenshot()

    
left = 48
top = 60
right = 190
bottom = 72
 
  
img = img.crop((left, top, right, bottom)) 
img.save("imageTest.png")
 
number = ""
output = ""
 
i = -7
while i < 129:
    i = i + 8
    j = i+9
    img_mod = img.crop((i, 0, j, 12))
    img_mod.save("images\cropTest" + str(i) + ".png")
    
    
    #print("i is: " + str(i))
    im = Image.open("images/cropTest" + str(i) + ".png")
    #im = Image.open("numberLibrary/9.png")
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
        
        value = value + isPixelWhite((pix[2, 10]))  
        value = value + isPixelWhite((pix[3, 2]))  
        value = value + isPixelWhite((pix[4, 4]))  
        value = value + isPixelWhite((pix[6, 10]))  
     
       
        if (value == 4):
            return True
        else: return False

    def isPixelTwo():
        value = 0
        
        value = value + isPixelWhite((pix[1, 3]))  
        value = value + isPixelWhite((pix[1, 10]))  
        value = value + isPixelWhite((pix[2, 7]))  
        value = value + isPixelWhite((pix[4, 6]))  
        value = value + isPixelWhite((pix[5, 10]))  
     
        
        if (value == 5):
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


    def checkNumbers():
        if isPixelZero():
            return 0
        elif isPixelOne():
            return 1
        elif isPixelTwo():
            return 2
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
    output = output.replace("\n", "")
output = output.replace("NoneNone", " -")
output = output.replace("None", ".")
print(output)
f.write(output + "\n")   
    #except Exception:
        #pass
   

#compare_images(original, shopped, "Original vs. Photoshopped")

#plt.show()