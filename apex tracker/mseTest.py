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
  

 
 
 
 
 
 
f = open("coords.txt", "a")


while True:
    try:
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
        library1 = cv2.imread("numberLibrary/1.png")
        library2 = cv2.imread("numberLibrary/2.png")
        library3 = cv2.imread("numberLibrary/3.png")
        library4 = cv2.imread("numberLibrary/4.png")
        library5 = cv2.imread("numberLibrary/5.png")
        library6 = cv2.imread("numberLibrary/6.png")
        library7 = cv2.imread("numberLibrary/7.png")
        library8 = cv2.imread("numberLibrary/8.png")
        library9 = cv2.imread("numberLibrary/9.png")
        library0 = cv2.imread("numberLibrary/0.png")
        libraryPeriod = cv2.imread("numberLibrary/period.png")
        libraryNegative = cv2.imread("numberLibrary/negative.png")
        #shopped = cv2.imread("black-and-white.png")
        # convert the images to grayscale
        original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        library1 = cv2.cvtColor(library1, cv2.COLOR_BGR2GRAY)
        library2 = cv2.cvtColor(library2, cv2.COLOR_BGR2GRAY)
        library3 = cv2.cvtColor(library3, cv2.COLOR_BGR2GRAY)
        library4 = cv2.cvtColor(library4, cv2.COLOR_BGR2GRAY)
        library5 = cv2.cvtColor(library5, cv2.COLOR_BGR2GRAY)
        library6 = cv2.cvtColor(library6, cv2.COLOR_BGR2GRAY)
        library7 = cv2.cvtColor(library7, cv2.COLOR_BGR2GRAY)
        library8 = cv2.cvtColor(library8, cv2.COLOR_BGR2GRAY)
        library9 = cv2.cvtColor(library9, cv2.COLOR_BGR2GRAY)
        library0 = cv2.cvtColor(library0, cv2.COLOR_BGR2GRAY)
        libraryPeriod = cv2.cvtColor(libraryPeriod, cv2.COLOR_BGR2GRAY)
        libraryNegative = cv2.cvtColor(libraryNegative, cv2.COLOR_BGR2GRAY)
        #shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

        # initialize the figure
        fig = plt.figure("Images")
        images = ("Original", original), ("library1", library1), ("library2", library2), ("library3", library3), ("library4", library4), ("library5", library5), ("library6", library6), ("library7", library7), ("library8", library8), ("library9", library9), ("library0", library0), ("libraryPeriod", libraryPeriod), ("libraryNegative", libraryNegative)
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
        i = -1
        space = 0
        while i < 142:
            i = i + 2
            j = i+9
            img_mod = img.crop((i, 0, j, 12))
            img_mod.save("images\cropTest" + str(i) + ".png")
            
            img_mod = cv2.imread("images\cropTest" + str(i) + ".png")
            img_mod = cv2.cvtColor(img_mod, cv2.COLOR_BGR2GRAY)
            
            
            #compare_images(img_mod, library6, "img_mod vs. library")
            #currentLibrary = "library" + str(l)
            while True:
                s = ssim(img_mod, library1)
                if s > 0.6:
                    print("1 " + str(i))
                    number = number + "1"
                    space = 0
                    break
                    
                s = ssim(img_mod, library2)
                if s > 0.6:
                    print("2 " + str(i))
                    number = number + "2"
                    space = 0
                    break
                    
                s = ssim(img_mod, library3)
                if s > 0.6:
                    print("3 " + str(i))
                    number = number + "3"
                    space = 0
                    break
                    
                s = ssim(img_mod, library4)
                if s > 0.6:
                    print("4 " + str(i))
                    number = number + "4"
                    space = 0
                    break
                    
                s = ssim(img_mod, library5)
                if s > 0.6:
                    print("5 " + str(i))
                    number = number + "5"
                    space = 0
                    break
                    
                s = ssim(img_mod, library6)
                if s > 0.6:
                    print("6 " + str(i))
                    number = number + "6"
                    space = 0
                    break
                    
                s = ssim(img_mod, library7)
                if s > 0.6:
                    print("7 " + str(i))
                    number = number + "7"
                    space = 0
                    break
                    
                s = ssim(img_mod, library8)
                if s > 0.6:
                    print("8 " + str(i))
                    number = number + "8"
                    space = 0
                    break
                    
                s = ssim(img_mod, library9)
                if s > 0.6:
                    print("9 " + str(i))
                    number = number + "9"
                    space = 0
                    break
                    
                s = ssim(img_mod, libraryPeriod)
                if s > 0.6:
                    print(". " + str(i))
                    number = number + "."
                    space = 0
                    break
                    
                s = ssim(img_mod, libraryNegative)
                if s > 0.6:
                    print("- " + str(i))
                    number = number + "-"
                    space = 0
                    break
                    
                space = space + 1
                if (space > 3):
                    number = number + " space "
                break
           
                
           


        f.write(number + "\n")
    
    except Exception:
        pass


f.close
    
#compare_images(original, shopped, "Original vs. Photoshopped")

#plt.show()