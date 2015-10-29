# -*- coding: utf-8 -*-
"""
Created on 2016-10-27

@author: Julian Altmeyer, Marcel Kieser
"""

import numpy as np
import matplotlib.pyplot as plt

#lese MessungsDaten
data = np.genfromtxt('Messungsdaten.txt', delimiter=",")

#lese OsziDaten
oszi = np.genfromtxt('MessungOszi.csv', delimiter=",")

# Anzeige
fig, ax = plt.subplots(figsize=(7,5))
ax.plot(data[:,0] , data[:,1], color = "orange", label="Einschwingvorgang ignoriert")
ax.plot(oszi[:,0] , oszi[:,1], color = "blue", label="Einschwingvorgang berücksichtigt")
ax.set_xlabel("Distanz [cm]")
ax.set_ylabel("Mittelwert der Spannung [V]")
ax.legend(loc='upper right');
