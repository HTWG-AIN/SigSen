# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:26:59 2015

@author: edc07
"""
import numpy as np
from TekTDS2000 import *

scope = TekTDS2000()

x,y = scope.getData(1,1000,2500)
np.savetxt("a4-len.csv" , np.transpose([x,y]), delimiter=",")

input()


x,y = scope.getData(1,1000,2500)
np.savetxt("a4-wid.csv" , np.transpose([x,y]), delimiter=",")