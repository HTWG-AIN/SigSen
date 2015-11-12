# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:07:39 2015

@author: Julian Altmeyer, Marcel Kieser
"""

import numpy as np
import cv2

def getSubImages(pic):
    image1 = pic[:,0:70]
    image2 = pic[:,90:230]
    image3 = pic[:,250:390]
    image4 = pic[:,410:550]
    image5 = pic[:,570:640]
    return image1, image2, image3, image4, image5


def getMeanStd(img):
    return np.mean(img), np.std(img)


def getTableLatex(table):
    strTab = ""
    for i in range(len(table)):
        strTab += "Unterbild " + str(i+1) + \
                  " & {0:.2f} & {1:.2f} \\\\\n\\hline\n".format(table[i][0],  table[i][1])

    print(strTab)

def maxContrast(img):
    maxValue = np.max(img)
    minValue = np.min(img)
    newImage = np.copy(img)
    
    for y in range(newImage.shape[0]):
        for x in range(newImage.shape[1]):
            if (maxValue - minValue) != 0:
                newImage[y][x] = (img[y][x] - minValue) * (255.0 / (maxValue - minValue))
            else:
                newImage[y][x] = 0
    return newImage


def versuch1():
    grayImg = cv2.imread("Grauwertkeil.png")    
    grayImg = cv2.cvtColor(grayImg, cv2.COLOR_BGR2GRAY)
    sliceAndTableImg(grayImg)

def sliceAndTableImg(image):    
    img1, img2, img3, img4, img5 = getSubImages(image)
    
    table = []
    table.append(getMeanStd(img1))
    table.append(getMeanStd(img2))
    table.append(getMeanStd(img3))
    table.append(getMeanStd(img4))
    table.append(getMeanStd(img5))
    
    getTableLatex(table)


def versuch2():
    dunkelbild = maxContrast(getDunkelbild())
    cv2.imwrite("DunkelbildContrastMax.png", dunkelbild)

def versuch3():
    weissbild = maxContrast(removeOffset(getWeissbild()))
    cv2.imwrite("WeissbildContrastMax.png", weissbild)
        

def versuch4():
    grayImg = cv2.imread("Grauwertkeil.png")
    grayImg = cv2.cvtColor(grayImg, cv2.COLOR_BGR2GRAY)
    dunkelbild = getDunkelbild()
    weissbild = getWeissbild()
    correctImg = correctImage(grayImg, weissbild, dunkelbild)
    cv2.imwrite("KorrigierterGrauwertkeil.png", correctImg)
    sliceAndTableImg(correctImg)

def correctImage(img, weisb, dunkelb):
    a = img - dunkelb
    a = a / normiereWeissbild(weisb)
    return a    
    
def normiereWeissbild(weissbild):
    w = np.double(weissbild)
    w = np.divide(w, np.mean(w))
    return w

def getWeissbild():
    weissbilder = []
    #erzeuge meanImage    
    for i in range(10):
        weissbilder.append(cv2.imread("Weissbilder/Weissbild" + str(i) + ".png"))
    
    meanImage = np.zeros((480, 640), dtype=int)

    for weissbild in weissbilder:
        wbild = cv2.cvtColor(weissbild, cv2.COLOR_BGR2GRAY)
        meanImage += wbild
        
    meanImage = meanImage / len(weissbilder)
    return meanImage

def getDunkelbild():
    dunkelbilder = []
    #erzeuge meanImage    
    for i in range(10):
        dunkelbilder.append(cv2.imread("Dunkelbilder/Dunkelbild" + str(i) + ".png"))

    meanImage = np.zeros((480, 640), dtype=int)

    for dunkelbild in dunkelbilder:
        dbild = cv2.cvtColor(dunkelbild, cv2.COLOR_BGR2GRAY)
        meanImage += dbild     
    
    meanImage = meanImage / len(dunkelbilder)
    return meanImage
    
def removeOffset(eingabebild):
    return eingabebild - getDunkelbild()

def main():
    
    versuch1()
    
    #versuch2()
    
    #versuch3()
    
    #versuch4()    
    
    #cv2.imshow("test", grayImg)
    #cv2.waitKey(5000)
    #cv2.destroyAllWindows()
    
    #cv2.imshow("test", maxContrast(grayImg))
    #cv2.waitKey(5000)
    #cv2.destroyAllWindows()

    #cv2.imwrite("Test/img1.png", img1)
    #cv2.imwrite("Test/img2.png", img2)
    #cv2.imwrite("Test/img3.png", img3)
    #cv2.imwrite("Test/img4.png", img4)
    #cv2.imwrite("Test/img5.png", img5)
    
    #cv2.imshow("frame", img[4])
    
    #while (True):
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', img1)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
         #   break


if __name__ == "__main__":
    main()


#def maxContrast(picture):
#    for pix in picture:
        #new_pix = ((pix - min) * (255.0/(max - min)))
 