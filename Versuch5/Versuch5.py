# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:15:07 2016

@author: edc07
"""


import numpy as np
import matplotlib.pyplot as plt

#import redlab as rl
#import time
#from TekTDS2000 import *


def versuch1():
    out(1)
    #print(str(get_input(4000, 8000)))
    print('fertig')


def versuch2():
    #print(str(np.mean(get_input(4000, 8000))))

    mult_array = np.array([0.103, 0.196, 0.2, 0.2, 0.194, 0.198, 0.199, 0.199, 0.2, 0.198])
    ad_array = np.array([0.015, 0.018, 0.013, 0.015, 0.016, 0.013, 0.012, 0.012, 0.014, 0.022])
    print("Multimeter Philips Std s={}".format(getStd(mult_array)))
    print("AD Wandler Std s={}".format(getStd(ad_array)))

def versuch3():
    da_array = np.array([0.011, 0.019, 0.027, 0.041, 0.049, 0.058, 0.072, 0.080, 0.090, 0.096])
    print("DA Wandler Std s={}".format(getStd(da_array)))

def versuch4():    
    for x in get_sin():
       out(x)
        time.sleep(0.01)
    
    save_input_oszi()
    print(getInputData('sinus.csv')[0])
    
    plotRecord(getInputData('sinus.csv'))


def versuch5():
    np.savetxt('8000.csv', rl.cbVInScan(0, 0, 0, 4000, 8000, 1))
    
    plotFFT(getInputData('1000.csv'), 8000,'1000fft.png')
    plotFFT(getInputData('2000.csv'), 8000,'2000fft.png')
    plotFFT(getInputData('3000.csv'), 8000,'3000fft.png')
    plotFFT(getInputData('4000.csv'), 8000,'4000fft.png')
    plotFFT(getInputData('5000.csv'), 8000,'5000fft.png')
    plotFFT(getInputData('6000.csv'), 8000,'6000fft.png')
    plotFFT(getInputData('7000.csv'), 8000,'7000fft.png')
    plotFFT(getInputData('8000.csv'), 8000,'8000fft.png')


def plotFFT(rec, sampleRate, filename=''):
    
    #fft
    # n = Anzahl der Schwingungen innerhalb der gesamten Signaldauer
    c = np.fft.fft(rec)
    n = np.abs(c)
    sampleTime = 1 / sampleRate
    
    count = np.arange(0, len(n))* (1 / (len(n) * sampleTime))
    
    # Anzahl der Schwingungen innerhalb der gesamten Signaldauer dargestellt
    dpi=75
    fig, axN = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    axN.plot(count[:],n[:], color = "blue", label=" Amplitudenspektrum ")
    # lässt X-Achse bei 0 beginnen
    axN.autoscale(enable=True, axis='x', tight=True)
    axN.legend(loc='upper right');
    axN.set_xlabel("Frequenz [Hz]")
    axN.set_ylabel("Amplitude")
    
    # als png abspeichern    
    if filename is not '':
        fig.savefig(filename, transparent=True, dpi=dpi)
    return


def getStd(e_array):
    return np.std(e_array)

def plotRecord(rec):
    myDpi = 75
    fig, ax = plt.subplots(figsize=(800/myDpi, 600/myDpi), dpi=myDpi)
    ax.autoscale(enable=True, axis='x', tight=True)
    ax.plot(rec[400:2100,0], rec[400:2100,1])
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
    versuch1()
    versuch2()
    versuch3()
    versuch4()
    versuch5()

if __name__ == '__main__':
    main()
