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
  

value = (255, 0, 0, 255)

im = Image.open("numberLibrary/3.png") # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
print (pix[7, 2])  # Get the RGBA Value of the a pixel of an image

pix[7,2] = value  # Set the RGBA Value of the image (tuple)
im.save('alive_parrot.png')  # Save the modified pixels as .png