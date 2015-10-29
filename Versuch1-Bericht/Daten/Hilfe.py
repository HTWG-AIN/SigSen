# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:42:41 2015

@author: Marcel
"""

import numpy as np


#lese MessungsDaten
data = np.genfromtxt('Messungsdaten.txt', delimiter=",")

oszi = np.genfromtxt('MessungOszi.csv', delimiter=",")


for x in range(20):
    print("{0:2.3f}".format(oszi[x,2]))