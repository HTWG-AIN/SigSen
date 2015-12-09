#-*-coding:utf-8-*-
"""
CreatedonMonDec714:09:282015

@author:edc10
"""

#import pyaudio
import numpy as np
import scipy.signal as win
import scipy.stats as stats
import matplotlib.pyplot as plt

#FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
SEC=2
READBYTES = int(44100*SEC)
TRIGGER = 800
WINDOWSIZE = 512
WINDOWTIME = WINDOWSIZE / SAMPLEFREQ


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


def getInputDataPyAudio():
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


def plotFFT2(rec, filename=''):  
    # spiegelung eleminieren
    half = len(rec)/2+1
    count = np.arange(0, int(half)) / WINDOWTIME
    
    # Anzahl der Schwingungen innerhalb der gesamten Signaldauer dargestellt
    dpi=75
    fig, axN = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    axN.plot(count[:],rec[:half], color = "blue", label=" Amplitudenspektrum ")
    # lässt X-Achse bei 0 beginnen
    axN.autoscale(enable=True, axis='x', tight=True)
    axN.legend(loc='upper right');
    axN.set_xlabel("Frequenz [Hz]")
    axN.set_ylabel("Amplitude [$|Y(f)|$]")
    
    # als png abspeichern    
    if filename is not '':
        fig.savefig(filename, transparent=True, dpi=dpi)
    return


def record5():
    for i in range(5):
        data = getInputDataPyAudio()
        triggered = trigger(data)
        cutted = cut(triggered)
        plotRecord(cutted)
        np.savetxt("TestMarcelRechts" + str(i) + ".csv", cutted, delimiter=",")
        print("fertig")
        input()
    return


def getInputData(filename):
    return np.genfromtxt(filename, delimiter=',')


def windowing(rec):
    steps = []
    for i in range(0, len(rec), int(WINDOWSIZE / 2)):
        steps.append(i)
    steps.append(len(rec))

    windows = []
    for i in range(len(steps) - 3):
        windows.append(rec[steps[i]:steps[i + 2]])

    #----------------------------------------------------

    for i in range(len(windows)):
        windows[i] = windows[i] * win.gaussian(WINDOWSIZE, std=WINDOWSIZE/4)
    
    result = np.zeros(WINDOWSIZE)
    for i in range(len(windows)):
        windows[i] = np.fft.fft(windows[i]/((2**15)-1))
        windows[i] = np.abs(windows[i])
        result = result + windows[i]
    
    result = result / len(windows)
    return result


def getMeans(pathname):
    files = ['Hoch', 'Tief', 'Links', 'Rechts']
    dic = {}
    for name in files:
        result = []
        for i in range(5):
            data = getInputData(pathname + name + str(i) + ".csv")
            result.append(windowing(data))
    
        summ = np.zeros(WINDOWSIZE)
        for res in result:
            summ = summ + res
        
        mean = summ / len(result)
        dic[name] = mean
    return dic


def speechRecognition(referenceDict, data):
    maximum = 0
    for key in referenceDict:
        coefficient = stats.pearsonr(referenceDict[key], data)[0]
        if coefficient > maximum:
            maximum = coefficient
            bestKey = key
    return bestKey


def versuch1a():
    decoded = getInputDataPyAudio()
    #np.savetxt("Aufnahme1.csv", decoded, delimiter=",")
    plotRecord(decoded)
    #plotRecord(decoded, 'v1.png')


def versuch1b():
    decoded = getInputDataPyAudio()
    triggered = trigger(decoded)
    cutted = cut(triggered)
    plotRecord(cutted)


def versuch1bc():
    data = np.genfromtxt('Aufnahme1.csv', delimiter=',')
    triggered = trigger(data)
    cutted = cut(triggered)
    plotRecord(cutted, 'Aufnahme1TriggerCut.png')
    np.savetxt("Aufnahme1TriggerCut.csv", cutted, delimiter=",")
    plotFFT(cutted, 'Aufnahme1TriggerCutFFT.png')


def versuch1d():
    data = getInputData('Aufnahme1TriggerCut.csv')
    data = windowing(data)
    plotFFT2(data)


def versuch2():
    reference = getMeans("Referenz/Referenz")
    #testJulian = getMeans("TestJulian/TestJulian")
    #testMarcel = getMeans("TestMarcel/TestMarcel")  
    
#    for key in reference:
#        plotFFT2(reference[key])
#        plotFFT2(testJulian[key])
#        plotFFT2(testMarcel[key])

    # Testdaten in Dictionaries abspeichern
    testJulian = {}
    testMarcel = {}
    for name in ['Hoch', 'Tief', 'Links', 'Rechts']:
        testJulian[name] = []
        testMarcel[name] = []
        for i in range(5):
            dataJulian = getInputData("TestJulian/TestJulian" + name + str(i) + ".csv")
            dataMarcel = getInputData("TestMarcel/TestMarcel" + name + str(i) + ".csv")
            dataJulian = windowing(dataJulian)
            dataMarcel = windowing(dataMarcel)
            testJulian[name].append(dataJulian)
            testMarcel[name].append(dataMarcel)

#    for key in reference:
#        for i in range(5):
#            print("Julian (" + key + "):" + str(stats.pearsonr(reference[key], testJulian[key][i])[0]))
#            print("Marcel (" + key + "):" + str(stats.pearsonr(reference[key], testMarcel[key][i])[0]))
#
#    r = stats.pearsonr(reference["Hoch"], reference["Links"])[0]
#    print(r)
#    
#    for key in testJulian:
#        plotFFT2(testJulian[key][0])
#        plotFFT(getInputData("TestJulian/TestJulian" + key + str(0) + ".csv"))
        
    # Spracherkennung
    for key in testMarcel:
        for i in range(5):
            print("Wort:" + key)
            print("Erkannt: " + speechRecognition(reference, testMarcel[key][i]))


def main():
    #versuch1a()
    #versuch1bc()
    #record5()
    #versuch1d()
    versuch2()


if __name__ == "__main__":
    main()
    