#!/usr/bin/python
# -*- coding: utf-8 -*-

# добавляет промежуточные значения E_a и 
# изменяет шаг по энергии нейтронов

from __future__ import print_function
from __future__ import division
import numpy as np
import math
from scipy import interpolate
from scipy import integrate
import sys
import os

# import plotter
# import constants
import processor
import chemistry
# sys.path.insert(0, '../neucbot/')
# import neucbot


def RebinXS(fname, MT, dE_a):

    MF = int(3)

    dirname = fname + "/MF" + str(MF) + "_MT" + str(MT)  # C_13/MF3_MT50

    f = open("./reshaped/" + dirname, "r")    # только что созданный файл в папке MF3_MT50 
    fileLen = 0 # число строк в файле
    for line in f.readlines():
        if line.split():
            fileLen += 1
    f.close()

    E_a = np.zeros(fileLen)
    X_S = np.zeros(fileLen)
    NS = 0
    f = open("./reshaped/" + dirname, "r")
    for line in f.readlines():  # считываем данные файла в массивы
        if line.split():
            E_a[NS] = line.split()[0]
            X_S[NS] = line.split()[1]
            NS += 1
    E_aRebin = np.arange(0, 15e6 + dE_a, dE_a)  # создаём массивы с равным шагом по энергии
    XS_Rebin = np.zeros_like(E_aRebin)

    minE_a = int(np.ceil (np.min(E_a)/dE_a)*dE_a)  # при целом dE_a всегда целое 
    maxE_a = int(np.floor(np.max(E_a)/dE_a)*dE_a)  # при целом dE_a всегда целое 

    E_nFunc = interpolate.interp1d(E_a, X_S)    # интерполяция на основе исходных данных
    XS_Rebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1] = \
        E_nFunc(E_aRebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1])  # заполняем сечения с равным шагом по энергии
    f.close()
    
    f1 = open("../neucbot/Data/Isotopes/" + \
                fname.split("_")[0] + "/" + \
                fname.replace("_", "") + \
                    "/JendlOut/(a,n0)XS", "w")    # ../neucbot/Data/Isotopes/C/C13/JendlOut/(a,n0)XS
    f1.write("# E_a, MeV\ttotal XS, mb\n")
    for i in range(len(E_aRebin)):
        f1.write(str(E_aRebin[i]/1e6) + " \t\t" + str(XS_Rebin[i]*1e3) + "\n")    # E_a, Mev   XS, mb
    f1.close()


# считывает из файла ./En_distribution/... массивы E_aBase, E_nBase, distBase
def readEnergyAngleDistribtion(fname, MT, points):  
    MF = int(6)

    dirname = "En_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT)
    dirLen = len([name for name in os.listdir(dirname)])    # число файлов в папке
    E_aBase = np.zeros(dirLen)  # массив энергий налетающих альфа частиц [в эВ]
    distBase = np.zeros((dirLen, points))   # массив Энерго-углового распределения [безразмерное]
    E_nBase = np.zeros((dirLen, points))    # массив энергий вылетающих нейтронов [в эВ]
    NK = 1  # есть в названии директории. Отвечает за количество различных вылетющих частц
    counter = 0 # счётчик по эенргии (NE)
    
    while True:   # пока не закончатся файлы в директории /En_distribution/fname/MF _MT /
        if not os.path.isfile(dirname + "/NK" + str(NK) + "_NE" + str(counter)):    
        
            # на будущее, когда будет несколько вылетающих частиц (не учтено сейчас!!! будет перезапись по counter)
            # когда прошли все E_in для нынешнего NK
            if os.path.isfile(dirname + "/NK" + str(NK+1) + "_NE0"):  
                NK += 1
                counter = 0
                print(fname, "MF", MF, "MT", MT, "contains data of more than one product particle")
                # сигнал, что вылетающих частиц больше одной
            else:
                break   # остановиться когда прошли все NK и E_in (=NE)
        
        f = open(dirname + "/NK" + str(NK) + "_NE" + str(counter), "r")
        NS = 0  # номер строки в файле
        for line in f.readlines():  # считываем построчно
            if (NS == 1):   # строка, где записана энергия влетающей альфа-частицы
                E_aBase[counter] = float(line)  # в эВ
            if (NS > 3 and line != ""):    # строки, где хранятся коэффициенты Лежандра 
                E_nBase[counter, NS-4] = line.split()[0]
                distBase[counter, NS-4] = line.split()[1]
            NS += 1
        counter += 1
        f.close()
    return E_aBase, E_nBase, distBase


# по названию частицы и типу реакции создаёт папки ./JendlOut с нейтронными спектрами [мб] в ./neucbot
def neucbotIn(fname, MT, points, dE_a, dE_n):   
    # fname = "C_13", MT=50, points = 101,  dE_a = dE_n = 10000eV
    MF = int(6)

    dirname = "En_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT)
    if not os.path.isdir(dirname):    
        # проверка наличия директории
        print ("Trying to obtain raw distribution for " + fname + "!")
        NK,NE,E_in,S,isData = processor.getEnergyAngleDistribtion(fname,MT,points,normcheck=False)
        processor.angle2spectrum(fname, MT, points, NK, NE, E_in, S, isData)
    if os.path.isdir(dirname):    
        # теперь файл есть, если соответствующие данные JENDL есть
        E_aBase, E_nBase, distBase = readEnergyAngleDistribtion(fname, MT, points)
        
        # E_aBase   [dirLen]            # Сырые данные,
        # E_nBase   [dirLen, points]    # разные интервалы по энергии,
        # distBase  [dirLen, points]    # фиксированное к-во точек (=200). 
        
        minE_a = int(np.ceil(np.min(E_aBase)/dE_a)*dE_a)  # при целом dE_a всегда целое 
        maxE_a = int(np.floor(np.max(E_aBase)/dE_a)*dE_a)  # при целом dE_a всегда целое 
        NEWminE_a = 0
        NEWmaxE_a = 15e6  
        newDirLength = int((NEWmaxE_a - NEWminE_a)/dE_a + 1)   # длина новой директории (./rebin/X_**)
        E_aRebin = np.linspace(NEWminE_a, NEWmaxE_a, newDirLength)   # массив энергий налетающих альфа частиц (с равным шагом = dE_a)
        E_nTransitional = np.zeros((newDirLength, points))  # промежуточный массив энергий нейтронов
        distTransitional= np.zeros((newDirLength, points))  # промежуточный массив ф-ции распределния по энергиям a и n
        
        for i in range(points): # алгоритм перебиновки
            E_nFunc = interpolate.interp1d(E_aBase, E_nBase[:,i])   # функция на основе сырых данных
            E_nTransitional[int(minE_a/dE_a):int(maxE_a/dE_a)+1,i] = \
                E_nFunc(E_aRebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1])  # заполняем промежуточный массив
            distFunc = interpolate.interp1d(E_aBase, distBase[:,i]) # функция на основе сырых данных
            distTransitional[int(minE_a/dE_a):int(maxE_a/dE_a)+1,i] = \
                distFunc(E_aRebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1]) # заполняем промежуточный массив
            
        NEWmaxE_n = 15e6    # максммальная энергия нейтрона = 15 МэВ
        # dE_n = 100e3    # размер бина по энергии нейтрона 100e3 eV = 0.1 MeV, как в NeuCBOT. Хорошо бы сделать поменьше
        
        newArrayLength = int(NEWmaxE_n/dE_n)   # max E_n (<= max E_a = 20 MeV) / dE_n = 100 keV
        E_nRebin = np.linspace(dE_n, NEWmaxE_n, newArrayLength) # эквидистантный по E_n со 100 кэВ до 15 МэВ
        distRebin = np.zeros((newDirLength, newArrayLength))    # массив идёт с шагом 1 эВ по энергии нейрона
        minE_n = np.zeros(newDirLength)
        maxE_n = np.zeros(newDirLength)
        for i in range(newDirLength):
            minE_n[i] = int(np.ceil (np.min(E_nTransitional[i])/dE_n)*dE_n)   # при dE_a>1eV всегда целое количество эВ
            maxE_n[i] = int(np.floor(np.max(E_nTransitional[i])/dE_n)*dE_n)   # при dE_a>1eV всегда целое количество эВ
            if (minE_a <= E_aRebin[i] and E_aRebin[i] <= maxE_a):
                NEWdistFunc = interpolate.interp1d(E_nTransitional[i], distTransitional[i])
                distRebin[i,int(minE_n[i]/dE_n):int(maxE_n[i]/dE_n)] = \
                NEWdistFunc(E_nRebin[int(minE_n[i]/dE_n):int(maxE_n[i]/dE_n)])
        
        E_nBinSize = 100e3  # размер бина в файле
        newFileLength = int(NEWmaxE_n/E_nBinSize)
        FIN_E_n = np.linspace(E_nBinSize, NEWmaxE_n, newFileLength) # от 0.1 до 15.0 МэВ с шагом 0.1 МэВ
        FINdist = np.zeros((newDirLength,newFileLength))
        for j in range(newFileLength):  # перебор по бинам энергий нейтронов
            for b in range(newArrayLength-1):
                if(FIN_E_n[j]-E_nBinSize <= E_nRebin[b] and E_nRebin[b] < FIN_E_n[j]):
                    FINdist[int(minE_a/dE_a):int(maxE_a/dE_a)+1,j] += \
                        (distRebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1,b] + \
                         distRebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1,b+1]) / 2.
        TotXS = np.zeros(newDirLength)
        NS = 0

        if not os.path.isdir("../neucbot/Data/Isotopes/" + \
                             fname.split("_")[0] + "/" + fname.replace("_", "") + "/JendlOut"):   
            os.mkdir("../neucbot/Data/Isotopes/" + \
                     fname.split("_")[0] + "/" + fname.replace("_", "") + "/JendlOut")

        RebinXS(fname, MT, dE_a)

        f = open("../neucbot/Data/Isotopes/" + \
                  fname.split("_")[0] + "/" + \
                    fname.replace("_", "") + \
                        "/JendlOut/(a,n0)XS", "r")    # ../neucbot/Data/Isotopes/C/C13/JendlOut/(a,n0)XS
        
        for line in f.readlines():  # считываем построчно
            if (line[0] != "#"):
                TotXS[NS] = float(line.split()[1])
                NS += 1
        f.close()

        for i in range(newDirLength):
            FINdist[i] *= TotXS[i]
            
        # if not os.path.isdir("rebin"):   
        #     os.mkdir("rebin")
        # if not os.path.isdir("rebin/" + fname):   
        #     os.mkdir("rebin/" + fname)
        # for i in range(newDirLength):
        #     f = open("rebin/" + fname + "/outputE" + str("{:.4f}".format(E_aRebin[i]/1e6)), "w")    # запись в папку ENDF6-reader/rebin/
            
            f = open("../neucbot/Data/Isotopes/" + fname.split("_")[0] + "/" + fname.replace("_", "") + \
                      "/JendlOut/outputE" + str("{:.4f}".format(E_aRebin[i]/1e6)), "w")    # запись в neucbot/
            
            if (minE_a > E_aRebin[i] or E_aRebin[i] > maxE_a or TotXS[i] == 0):
                f.write("EMPTY")
            else:    
                f.write("# Incident particle energy (MeV) = \n# " + str(E_aRebin[i]/1e6) + "\n#\n" +\
                        "# En.lab,MeV distribution\n")
                for j in range(newFileLength): 
                    f.write(str("{:11.6f}".format(FIN_E_n[j]/1e6)) + "  " + \
                            str(FINdist[i,j]*1e6) + "\n")   # перевод эВ->МэВ для сохранения нормировки
            f.close()