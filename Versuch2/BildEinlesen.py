# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:07:39 2015

@author: edc07
"""

import numpy as np
import cv2
#import pyopencv

#image = pyopencv.imread("Grauwertkeil.png")

def getSubImages(pic):
    image1 = pic[:,0:70]
    image2 = pic[:,90:230]
    image3 = pic[:,250:390]
    image4 = pic[:,410:550]
    image5 = pic[:,570:640]
    return image1, image2, image3, image4, image5

image = cv2.imread("Grauwertkeil.png")



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape)
print(gray)

img1, img2, img3, img4, img5 = getSubImages(gray)

cv2.imwrite("Test/img1.png", img1)
cv2.imwrite("Test/img2.png", img2)
cv2.imwrite("Test/img3.png", img3)
cv2.imwrite("Test/img4.png", img4)
cv2.imwrite("Test/img5.png", img5)

#cv2.imshow("frame", img[4])

#while (True):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', img1)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break

np.mean(gray)



#def maxContrast(picture):
#    for pix in picture:
        #new_pix = ((pix - min) * (255.0/(max - min)))
 