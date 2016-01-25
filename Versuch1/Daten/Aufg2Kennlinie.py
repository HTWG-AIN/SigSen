# -*- coding: utf-8 -*-
"""
Created on 2016-10-27

@author: Julian Altmeyer, Marcel Kieser
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

#lade BeispielDaten
data = np.genfromtxt('MessungOszi.csv', delimiter=",")
print(data)

#Kopie Logarithmieren
#!!!! so: log = data
#gehts nicht, da Objekt refernz kopiert wird
# deshalb:

#log = np.copy(data)

# y = Distanz in cm
logy = np.log(data[:,0])
# x = Spannung in V
logx = np.log(data[:,1])

#for row_idx, row in enumerate(log):
#    for col_idx, col in enumerate(row):
#        log[row_idx,col_idx] = math.log(col)
print(logx)
print(logy)

# beide kurven abbilden
# Rahmen bauen
fig, ax = plt.subplots(figsize=(7,5))
# daten ausgeben plot(x,y)
#print(data[:,1])
ax.plot(data[:,1] , data[:,0], color = "blue", label = "original")
ax.plot(logx, logy, color = "orange", linestyle = "-", linewidth = 2.3, label = "logarithmiert")
ax.set_xlabel("Spannung [V]")
ax.set_ylabel("Distanz [cm] ")
ax.legend(loc='upper right')
#nochmal log in gross
fig, ax = plt.subplots(figsize=(5,5))
ax.plot(logx, logy, color = "orange", linestyle = "-", linewidth = 2.3, label = "logarithmiert")
ax.set_xlabel("Spannung [V]")
ax.set_ylabel("Distanz [cm] ")
ax.legend(loc='upper right')

#
# lineare reg
#

# a = steigung,b = schnittpunkt,korrelationskoeffizient,p-wert,Standart Fehler
# linData = stats.linregress(data)
a,b,r,p,R2 = stats.linregress(logx,logy)
print("a = "+ str(a))
print("b = "+ str(b))

#fkt fuer berechnung der neuen y werte, welche die alten annähernd beschreiben sollten
def umkehrFkt(x):
    return (math.exp(b)*(x**a))

#generiere Kennlinie
xValues = np.linspace(0.4,1.5,50)
res = np.zeros((50,2))

for x in range(len(xValues)):
    res[x,0] = xValues[x]
    res[x,1] = umkehrFkt(xValues[x])


#Anzeige
fig, ax = plt.subplots(figsize=(7,5))
# daten ausgeben plot(x,y)
ax.plot(data[:,1] , data[:,0], color = "orange", label = "Gemessene Kennlinie")
ax.plot(res[:,0] , res[:,1], color = "blue", label = "Berechnete Kennlinie")
ax.set_xlabel("Spannung [V]")
ax.set_ylabel("Distanz [cm] ")
ax.legend(loc='upper right');

