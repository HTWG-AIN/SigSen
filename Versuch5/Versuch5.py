# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:15:07 2016

@author: edc07
"""

import redlab as rl
import numpy as np
import time
from TekTDS2000 import *


def versuch1():
    out(1)
    #print(str(get_input(4000, 8000)))
    print('fertig')


def versuch2():
    print(str(np.mean(get_input(4000, 8000))))


def versuch4():    
    #for x in get_sin():
    #   out(x)
    #    time.sleep(0.01)
    
    #save_input_oszi()
    #print(getInputData('sinus.csv')[0])
    plotRecord(getInputData('sinus.csv'))


def versuch5():
    np.savetxt('8000.csv', rl.cbVInScan(0, 0, 0, 4000, 8000, 1))


def plotRecord(rec):
    myDpi = 75
    fig, ax = plt.subplots(figsize=(800/myDpi, 600/myDpi), dpi=myDpi)
    ax.autoscale(enable=True, axis='x', tight=True)
    ax.plot(rec)
    ax.set_xlabel('Time [$s$]')
    ax.set_ylabel('Amplitude [$V$]')


def save_input_oszi():
    scope = TekTDS2000()

    x,y = scope.getData(1,1,2500)
    np.savetxt("sinus.csv" , np.transpose([x,y]), delimiter=",")


def getInputData(filename):
    return np.genfromtxt(filename, delimiter=',')


def get_input(number, samplerate):
    return rl.cbVInScan(0, 0, 0, number, samplerate, 1)


def out(voltage):
    rl.cbVOut(0, 0, 101, voltage)


def get_sin(fs=100):
    val = np.linspace(0, 2 * np.pi, fs)
    return np.sin(val) + 1


def main():
    #versuch1()
    #versuch2()
    versuch4()


if __name__ == '__main__':
    main()
