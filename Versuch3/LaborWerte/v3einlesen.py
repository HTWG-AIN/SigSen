# -*- coding: utf-8 -*-
"""
Created on 2016-10-27
@author: Julian Altmeyer, Marcel Kieser
"""

import numpy as np
import matplotlib.pyplot as plt

#lese MessungsDaten
#data = np.genfromtxt('Messungsdaten.txt', delimiter=",")

#lese OsziDaten
oszi = np.genfromtxt('v3_mundharm_tonhoehe2.csv', delimiter=",")

# Anzeige
dpi=75
fig, ax = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
#ax.plot(data[:,0] , data[:,1], color = "orange", label="Einschwingvorgang ignoriert")
ax.plot(oszi[:,0] , oszi[:,1], color = "blue", label="Oszilloskop Einschwingvorgang berücksichtigt")
ax.autoscale(enable=True, axis='x', tight=True)
ax.set_xlabel("Distanz [cm]")
ax.set_ylabel("Mittelwert der Spannung [V]")
ax.legend(loc='upper right');
plt.savefig('V1_Signal.png', dpi=dpi)