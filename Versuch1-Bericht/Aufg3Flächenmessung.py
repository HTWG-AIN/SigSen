# -*- coding: utf-8 -*-
"""
Created on 2016-10-27

@author: Julian Altmeyer, Marcel Kieser
"""

import numpy as np
import math

# Kennlinien Parameter
a = -1.60
b = 3.00

#fkt
def umkehrFkt(x):
    return (math.exp(b)*(x**a))

def fehlerFkt(x, d):
    return np.sqrt((a * math.exp(b)*(x**(a-1))*d)**2)

# Länge #####################################################
#lade BeispielDaten
data = np.genfromtxt('a4-len.csv', delimiter=",")

#empirische Standardabweichung
sta = np.std(data[:,1])


#Standardabweichung für den Mittelwert
# n ist die Anzahl der Spannungswerte
n, m = data.shape
sta = sta/np.sqrt(n)

print(sta)

#
# Vertrauensbereich ermitteln
#
# Mittelwert berechnen
mean = np.mean(data[:,1])

#korregierte Angabe
delta = 1.0 * sta

print("fuer 68,26% gilt:")
print("x = " + str(mean) + " +- " + str(delta)+ " [V]")

#korregierte Angabe
delta2 = 1.96 * 2*sta

print("fuer 95% gilt:")
print("x = " + str(mean) + " +- " + str(delta2) + " [V]")

print(umkehrFkt(mean))
print(fehlerFkt(mean,delta))
print(fehlerFkt(mean,delta2))
print()

# Breite #######################################################
#lade BeispielDaten
data = np.genfromtxt('a4-wid.csv', delimiter=",")

#empirische Standardabweichung
sta = np.std(data[:,1])

#Standardabweichung für den Mittelwert
# n ist die Anzahl der Spannungswerte
n, m = data.shape
sta = sta/np.sqrt(n)

print(sta)

#
# Vertrauensbereich ermitteln
#
# Mittelwert berechnen
mean2 = np.mean(data[:,1])

#korregierte Angabe
deltaW = 1.0 * sta

print("fuer 68,26% gilt:")
print("x = " + str(mean2) + " +- " + str(deltaW)+ " [V]")

#korregierte Angabe
deltaW2 = 1.96 * 2*sta

print("fuer 95% gilt:")
print("x = " + str(mean2) + " +- " + str(deltaW2) + " [V]")

print(umkehrFkt(mean2))
print(fehlerFkt(mean2,deltaW))
print(fehlerFkt(mean2,deltaW2))
print()

#3b ###########################################################
#TODO relative Fehler???
def fehlerFkt2(x, d, x2, d2):
    return np.sqrt(((a * (x2**a) * math.exp(2*b)*(x**(a-1))*d)**2)* ((a *(x**a) * math.exp(2*b)*(x2**(a-1))*d2)**2))

print(umkehrFkt(mean)*umkehrFkt(mean2))
print(fehlerFkt2(mean,delta,mean2,deltaW))
print(fehlerFkt2(mean,delta2,mean2,deltaW2))

































