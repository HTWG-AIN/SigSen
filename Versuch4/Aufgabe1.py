#-*-coding:utf-8-*-
"""
CreatedonMonDec714:09:282015

@author:edc10
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
SEC=2
READBYTES = int(44100*SEC)
TRIGGER = 800


def plotRecord(rec, filename=''):
    myDpi = 75
    fig, ax = plt.subplots(figsize=(800/myDpi, 600/myDpi), dpi=myDpi)
    ax.autoscale(enable=True, axis='x', tight=True)
    time = np.linspace(0, len(rec)/SAMPLEFREQ, len(rec))
    amp = rec/((2**15)-1)
    ax.plot(time, amp)
    ax.set_xlabel('Time [$s$]')
    ax.set_ylabel('Amplitude [$V$]')
    if filename is not '':
        fig.savefig(filename, transparent=True, dpi=myDpi)
    return
    
    
def trigger(rec):
    for i in range(len(rec)):
        if rec[i] > TRIGGER:
            return rec[i:]
    return []


def cut(rec):
    if len(rec) < SAMPLEFREQ:
        size = SAMPLEFREQ - len(rec)
        rec = np.append(rec, np.zeros(size))

    return rec[:SAMPLEFREQ]


def getInputData():
    p = pyaudio.PyAudio()
    print('running')
    
    stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                    input=True, frames_per_buffer=READBYTES)
    data = stream.read(READBYTES)
    decoded = np.fromstring(data, 'Int16')

    stream.stop_stream()
    stream.close()
    p.terminate()
    print('done')
    return decoded


def plotFFT(rec, filename=''):
    
    #fft
    # n = Anzahl der Schwingungen innerhalb der gesamten Signaldauer
    amp = rec/((2**15)-1)
    c = np.fft.fft(amp)
    n = np.abs(c)
    
    # spiegelung eleminieren
    half = len(n)/2+1
    #print(half)
    count = np.arange(0, int(half))
    #print(count)
    
    # Anzahl der Schwingungen innerhalb der gesamten Signaldauer dargestellt
    dpi=75
    fig, axN = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    axN.plot(count[:],n[:half], color = "blue", label=" Amplitudenspektrum ")
    # lässt X-Achse bei 0 beginnen
    axN.autoscale(enable=True, axis='x', tight=True)
    axN.legend(loc='upper right');
    axN.set_xlabel("Frequenz [Hz]")
    axN.set_ylabel("Amplitude [$|Y(f)|$]")
    
    # als png abspeichern    
    if filename is not '':
        fig.savefig(filename, transparent=True, dpi=dpi)
    return


def versuch1a():
    decoded = getInputData()
    #np.savetxt("Aufnahme1.csv", decoded, delimiter=",")
    plotRecord(decoded)
    #plotRecord(decoded, 'v1.png')


def versuch1b():
    decoded = getInputData()
    triggered = trigger(decoded)
    cutted = cut(triggered)
    plotRecord(cutted)


def versuch1b2():
    data = np.genfromtxt('Aufnahme1.csv', delimiter=',')
    triggered = trigger(data)
    cutted = cut(triggered)
    plotRecord(cutted)
    plotFFT(cutted)


def record5():
    for i in range(5):
        data = getInputData()
        triggered = trigger(data)
        cutted = cut(triggered)
        plotRecord(cutted)
        np.savetxt("TestMarcelRechts" + str(i) + ".csv", cutted, delimiter=",")
        print("fertig")
        input()
    return


def main():
    #versuch1a()
    #versuch1b2()
    record5()


if __name__ == "__main__":
    main()
    