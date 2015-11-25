# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:23:13 2015

@author: edc07
"""
import numpy as np
from TekTDS2000 import *

scope = TekTDS2000()

# warte auf irgend eine Eingabe
input()

# lese daten von oszi
x,y = scope.getData(1,1,2500)
# schreibe daten in ein csv
np.savetxt("v3_mundharm_tonhoehe2" + ".csv" , np.transpose([x,y]), delimiter=",")