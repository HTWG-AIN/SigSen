# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:22:49 2015

@author: edc07
"""

import cv2

cap = cv2.VideoCapture(0)

print("framewidth:" + str(cap.get(3)))
print("frameheight:" + str(cap.get(4)))
print("--------------------------------")
print("brightness:" + str(cap.get(10)))
print("contrast:" + str(cap.get(11)))
print("saturation:" + str(cap.get(12)))
print("--------------------------------")
print("gain:" + str(cap.get(14)))
print("exposure:" + str(cap.get(15)))
print("--------------------------------")
print("whitebalance:" + str(cap.get(17)))

cap.release()