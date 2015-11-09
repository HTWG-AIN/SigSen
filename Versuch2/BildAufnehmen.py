# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:16:52 2015

@author: edc07
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#for i in range(10):
#    ret, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   cv2.imwrite("Dunkelbilder/Dunkelbild" + str(i) + ".png", gray)

for i in range(10):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Weissbilder/Weissbild" + str(i) + ".png", gray)

cap.release()
cv2.destroyAllWindows()