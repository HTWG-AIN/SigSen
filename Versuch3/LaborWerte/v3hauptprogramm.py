# -*- coding: utf-8 -*-
"""
Created on 2016-10-27
@author: Julian Altmeyer, Marcel Kieser
"""

import numpy as np
import matplotlib.pyplot as plt


def versuch1_1():
    #lese OsziDaten aus csv
    oszi = np.genfromtxt('v3_mundharm_tonhoehe2.csv', delimiter=",")
    
    # Anzeige
    dpi=75
    fig, ax = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    ax.plot(oszi[:,0] , oszi[:,1], color = "blue", label="Signal f(t) eines Tons aus Mundharmonika")
    # lässt X-Achse bei 0 beginnen
    ax.autoscale(enable=True, axis='x', tight=True)
    ax.set_xlabel("t [s]")
    ax.set_ylabel("Spannung [V]")
    ax.legend(loc='upper right');
    
    # als png abspeichern
    #plt.savefig('V1_Signal_grundfrequenz.png', dpi=dpi)
    plt.savefig('V1_Signal_komp.png', dpi=dpi)

def versuch1_2():
    #lese OsziDaten aus csv
    oszi = np.genfromtxt('v3_mundharm_tonhoehe2.csv', delimiter=",")
    
    #fft
    # n = Anzahl der Schwingungen innerhalb der gesamten Signaldauer
    c = np.fft.fft(oszi[:,1])
    n = np.abs(c)
    
    # spiegelung eleminieren
    half = len(n)/2+1
    print(half)
    count = np.arange(0, int(half)) / 0.025
    print(count)
    
    # Anzahl der Schwingungen innerhalb der gesamten Signaldauer dargestellt
    dpi=75
    fig, axN = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    axN.semilogx(count[:],n[:half], color = "blue", label=" Amplitudenspektrum ")
    # lässt X-Achse bei 0 beginnen
    axN.autoscale(enable=True, axis='x', tight=True)
    axN.legend(loc='upper right');
    axN.set_xlabel("Frequenz [Hz]")
    axN.set_ylabel("Spannung [V]")
    
    # als png abspeichern    
    plt.savefig('V1_2_Amplitudenspektrum.png', dpi=dpi)

def versuch2(file):
    # einlesen der Messwerte
    l = np.genfromtxt(file, delimiter=",")
    l[:,1] = l[:,1]/1000 # V
    l[:,1] = 20 * np.log10(l[:,1]) # dB
    l[:,2] = l[:,2]/1000 # s

    #print(l)
    
    # Amplitudengang log
    dpi=75
    fig, ax = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    ax.semilogx(l[:,0], l[:,1], color = "blue", label=" xxx ")
    ax.set_xlabel("Frequenz [Hz]")
    ax.set_ylabel("Amplitude [dB]")
        
    # umrechnen von Delta-t nach Grad
    l[:,2] = -1 * l[:,2]*l[:,0]*360
    #print(l)
    
    # Phasengang log
    fig, ax2 = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    ax2.semilogx(l[:,0], l[:,2], color = "blue", label=" xxx ")
    ax2.set_xlabel("Frequenz [Hz]")
    ax2.set_ylabel(" Winkel Phi [°]")
    #plt.plot(l[:,0], l[:,1])
    #plt.plot(l[:,0], l[:,2])
        
    # Amplitudengang     

def main():    
    versuch1_1()
    #versuch1_2()
    #versuch2('Aufg2_Messungen/1Lautsprecher_Messwerte.csv')
    #versuch2('Aufg2_Messungen/2Lautsprecher_Messwerte.csv')
    
    
if __name__ == "__main__":
    main()