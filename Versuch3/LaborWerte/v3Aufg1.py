# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:23:13 2015

@author: edc07
"""
import numpy as np
from TekTDS2000 import *

scope = TekTDS2000()

input()
x,y = scope.getData(1,1,2500)
np.savetxt("v3_mundharm_tonhoehe2" + ".csv" , np.transpose([x,y]), delimiter=",")



#res = np.zeros((20,3))
#dists = np.linspace(10,70,20)

#for i in range(len(dists)):
    #print("Abstand" + str(dists[i]))
    #input()
    #x,y = scope.getData(1,0,2500)
    #np.savetxt("v3_mundharm_tonhoehe_" + str(dists[i]) + "https://github.com/redscarwolf/SigSen/blob/master/Versuch1-Bericht/Daten/Aufg1Einlesen.py.csv" , np.transpose([x,y]), delimiter=",")
    #res[i,0] = dists[i]
    #res[i,1] = np.mean(y)
    #res[i,2] = np.max(y) -np.min(y) # Delta V

#np.savetxt("v2data.csv", res, delimiter=",")
#scope.plot(1, filename="v1Signal.png")