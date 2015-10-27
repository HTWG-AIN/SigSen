# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

#TODO unklar %
#%matplotlib inline

#lese nach ersten 1000 die Daten ein
data = np.genfromtxt('stockholm_td_adj.dat', skip_header = 1000 )
print(data[:,6])
# data ist vom typ ndarray
# lese aus tuple die hoehe x und die breite y
x,y= data.shape

#Mittelwert
m = np.mean(data[:,5])
print(m)
mAchse = np.linspace(m,m,x)

#Standartabweichung
sta = np.std(data[:,5])
print(sta)

# generiere array von 0 bis groesse x-1
xAchse = np.arange(0,x)
#info
print(xAchse)

# Anzeige
# Rahmen bauen
fig, ax = plt.subplots(figsize=(15,5))
# daten ausgeben plot(x,y)
ax.plot(xAchse , data[:,5], color = "blue")
ax.plot(xAchse , mAchse, color = "orange", linestyle = "-", linewidth = 2.3)
