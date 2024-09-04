#!/usr/bin/python
# -*- coding: utf-8 -*-

# финальный этап работы ENDF6reader. 
# Интерполирует данные из stage_1_data/En_distribution 
# и записывает их в ../neucbot и в ./stage_2_data

from __future__ import print_function
from __future__ import division
import numpy as np
from scipy import interpolate
import os

import constants
import processor


# Делает массивы Ea_Rebin и XS_Rebin и записывает их в neucbot и в stage_2_data
def RebinXS(fname, MT, dE_a):
    MF = int(3)

    dirname = fname + "/MF" + str(MF) + "_MT" + str(MT)  # C_13/MF3_MT50

    f = open("./stage_1_data/reshaped/" + dirname, "r")    # только что созданный файл в папке MF3_MT50 
    fileLen = 0 # число строк в файле
    for line in f.readlines():
        if line.split():
            fileLen += 1
    f.close()

    E_a = np.zeros(fileLen)
    X_S = np.zeros(fileLen)
    NS = 0
    f = open("./stage_1_data/reshaped/" + dirname, "r")
    for line in f.readlines():  # считываем данные файла в массивы
        if line.split():
            E_a[NS] = line.split()[0]
            X_S[NS] = line.split()[1]
            NS += 1
    E_aRebin = np.arange(0, 15e6 + dE_a, dE_a)  # создаём массивы с равным шагом по энергии
    XS_Rebin = np.zeros_like(E_aRebin)

    minE_a = int(np.ceil (np.min(E_a)/dE_a)*dE_a)  # при целом dE_a всегда целое 
    maxE_a = int(np.floor(np.max(E_a)/dE_a)*dE_a)  # при целом dE_a всегда целое 
    minBinEa = int(minE_a/dE_a)     # для упрощения записи следующих строчек
    maxBinEa = int(maxE_a/dE_a)+1   # для упрощения записи следующих строчек

    E_nFunc = interpolate.interp1d(E_a, X_S)    # интерполяция на основе исходных данных
    XS_Rebin[minBinEa:maxBinEa+1] = \
        E_nFunc(E_aRebin[minBinEa:maxBinEa+1])  # заполняем сечения с равным шагом по энергии
    f.close()
    
    if not os.path.isdir("../neucbot/Data/Isotopes/" + \
                            fname.split("_")[0] + "/" + fname.replace("_", "") + "/JendlOut"):   
        os.mkdir("../neucbot/Data/Isotopes/" + \
                    fname.split("_")[0] + "/" + fname.replace("_", "") + "/JendlOut")
    
    if not os.path.isdir("./stage_2_data"):
        os.mkdir("./stage_2_data")
    if not os.path.isdir("./stage_2_data/" + fname):
        os.mkdir("./stage_2_data/" + fname )
    if not os.path.isdir("./stage_2_data/" + fname + "/MT" + str(MT)):
        os.mkdir("./stage_2_data/" + fname + "/MT" + str(MT))
        
    f1 = open("../neucbot/Data/Isotopes/" + \
                fname.split("_")[0] + "/" + \
                fname.replace("_", "") + \
                    "/JendlOut/(a,n0)XS", "w")    # ../neucbot/Data/Isotopes/C/C13/JendlOut/(a,n0)XS
    f2 = open("./stage_2_data/" + fname + "/MT" + \
                str(MT) + "/(a,n" + \
                str(MT-50) +")XS", "w")    # ./stage_2_data/C_13/MT51/(a,n1)XS
    
    f1.write("# E_a, MeV\t\tXS, mb\n")
    f2.write("# E_a, MeV\t\tXS, mb\n")

    for i in range(len(E_aRebin)):
        f1.write(str(E_aRebin[i]/constants.physics.MeV_to_eV) + " \t\t" + str(XS_Rebin[i]*constants.physics.b_to_mb) + "\n")    # E_a, Mev   XS, mb
        f2.write(str(E_aRebin[i]/constants.physics.MeV_to_eV) + " \t\t" + str(XS_Rebin[i]*constants.physics.b_to_mb) + "\n")    # E_a, Mev   XS, mb
    f1.close()
    f2.close()

    return XS_Rebin*constants.physics.b_to_mb # ? правильно ли умножится?


def interpolation(E_aBase, E_nBase, distBase, points, dE_a, dE_n):
    # E_aBase   [dirLen]            # Сырые данные,
    # E_nBase   [dirLen, points]    # разные интервалы по энергии,
    # distBase  [dirLen, points]    # фиксированное к-во точек (=201). 
    minE_a = int(np.ceil (np.min(E_aBase)/dE_a)*dE_a)  # при целом dE_a всегда целое 
    maxE_a = int(np.floor(np.max(E_aBase)/dE_a)*dE_a)  # при целом dE_a всегда целое 
    minBinEa = int(minE_a/dE_a)     # для упрощения записи следующих строчек
    maxBinEa = int(maxE_a/dE_a)+1   # для упрощения записи следующих строчек

    NEWminE_a = 0
    NEWmaxE_a = 15e6
    newDirLength = int((NEWmaxE_a - NEWminE_a)/dE_a + 1)   # длина новой директории (./stage_2_data/X_**)
    E_aRebin = np.linspace(NEWminE_a, NEWmaxE_a, newDirLength)   # массив энергий налетающих альфа частиц (с равным шагом = dE_a)
    E_nTransitional = np.zeros((newDirLength, points))  # промежуточный массив энергий нейтронов
    distTransitional= np.zeros((newDirLength, points))  # промежуточный массив ф-ции распределния по энергиям a и n
    
    for i in range(points): # алгоритм интерполяции
        E_nFunc = interpolate.interp1d(E_aBase, E_nBase[:,i])   # функция на основе сырых данных
        E_nTransitional[minBinEa:maxBinEa+1,i] = \
            E_nFunc(E_aRebin[minBinEa:maxBinEa+1])  # заполняем промежуточный массив
        distFunc = interpolate.interp1d(E_aBase, distBase[:,i]) # функция на основе сырых данных
        distTransitional[minBinEa:maxBinEa+1,i] = \
            distFunc(E_aRebin[minBinEa:maxBinEa+1]) # заполняем промежуточный массив
        
    NEWmaxE_n = 15e6    # максммальная энергия нейтрона = 15 МэВ ??
    # dE_n = 100e3    # размер бина по энергии нейтрона 100e3 eV = 0.1 MeV, как в NeuCBOT. Хорошо бы сделать поменьше
    
    newArrayLength = int(NEWmaxE_n/dE_n)   # max E_n (<= max E_a = 20 MeV) / dE_n = 100 keV
    E_nRebin = np.linspace(dE_n, NEWmaxE_n, newArrayLength) # эквидистантный по E_n со 100 кэВ до 15 МэВ
    distRebin = np.zeros((newDirLength, newArrayLength))    # массив идёт с шагом 1 эВ по энергии нейрона
    minE_n = np.zeros(newDirLength)
    maxE_n = np.zeros(newDirLength)
    for i in range(newDirLength):
        minE_n[i] = int(np.ceil (np.min(E_nTransitional[i])/dE_n)*dE_n)   # при dE_a>1eV всегда целое количество эВ
        maxE_n[i] = int(np.floor(np.max(E_nTransitional[i])/dE_n)*dE_n)   # при dE_a>1eV всегда целое количество эВ
        minBinEn = int(minE_n[i]/dE_n)-1  # для упрощения записи следующих строчек
        maxBinEn = int(maxE_n[i]/dE_n)    # для упрощения записи следующих строчек
        if (minE_a <= E_aRebin[i] and E_aRebin[i] <= maxE_a):
            NEWdistFunc = interpolate.interp1d(E_nTransitional[i], distTransitional[i])
            distRebin[i, minBinEn:maxBinEn] = \
            NEWdistFunc(E_nRebin[minBinEn:maxBinEn])
    
    # E_nBinSize = 100e3  # размер бина в файле
    # newFileLength = int(NEWmaxE_n/E_nBinSize)
    # FIN_E_n = np.linspace(E_nBinSize, NEWmaxE_n, newFileLength) # от 0.1 до 15.0 МэВ с шагом 0.1 МэВ
    # FINdist = np.zeros((newDirLength,newFileLength))
    # for j in range(newFileLength):  # перебор по бинам энергий нейтронов
    #     for b in range(newArrayLength-1):
    #         if(FIN_E_n[j]-E_nBinSize <= E_nRebin[b] and E_nRebin[b] < FIN_E_n[j]):
    #             FINdist[int(minE_a/dE_a):int(maxE_a/dE_a)+1,j] += \
    #                 (distRebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1,b] + \
    #                  distRebin[int(minE_a/dE_a):int(maxE_a/dE_a)+1,b+1]) / 2.
    return E_aRebin, E_nRebin, distRebin, minE_a, maxE_a, newDirLength, newArrayLength


# считывает из файла ./stage_1_data/En_distribution/... массивы E_aBase, E_nBase, distBase
def readNeutronEnergyDistribtion(fname, MT, points):  
    MF = int(6)

    dirname = "stage_1_data/En_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT)
    dirLen = len([name for name in os.listdir(dirname)])    # число файлов в папке
    E_aBase = np.zeros(dirLen)  # массив энергий налетающих альфа частиц [в эВ]
    distBase = np.zeros((dirLen, points))   # массив Энерго-углового распределения [безразмерное]
    E_nBase = np.zeros((dirLen, points))    # массив энергий вылетающих нейтронов [в эВ]
    NK = 1  # есть в названии директории. Отвечает за количество различных вылетющих частц
    counter = 0 # счётчик по эенргии (NE)
    
    while True:   # пока не закончатся файлы в директории /stage_1_data/En_distribution/fname/MF*_MT**/
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

    dirname = "stage_1_data/En_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT)
    if not os.path.isdir(dirname):    
        # проверка наличия директории
        print ("Trying to obtain raw distribution for " + fname + "!")
        processor.getEnergyAngleDistribtion(fname,MT,points,normcheck=False)
    if os.path.isdir(dirname):    
        # теперь файл есть, если соответствующие данные JENDL есть
        E_aBase, E_nBase, distBase = \
            readNeutronEnergyDistribtion(fname, MT, points)
        E_aRebin, E_nRebin, distRebin, minE_a, maxE_a, newDirLength, newArrayLength = \
            interpolation(E_aBase, E_nBase, distBase, points, dE_a, dE_n)
        XS_Rebin = RebinXS(fname, MT, dE_a)

        for i in range(newDirLength):
            distRebin[i] *= XS_Rebin[i]

            f1 = open("../neucbot/Data/Isotopes/" + fname.split("_")[0] + "/" + fname.replace("_", "") + \
                      "/JendlOut/outputE" + str("{:.4f}".format(E_aRebin[i]/constants.physics.MeV_to_eV)), "w")    # запись в neucbot/
            f2 = open("./stage_2_data/" + fname + "/MT" + str(MT) + "/outputE" + str("{:.4f}".format(E_aRebin[i]/constants.physics.MeV_to_eV)), "w")    # запись в neucbot/
            
            if (minE_a > E_aRebin[i] or E_aRebin[i] > maxE_a or XS_Rebin[i] == 0):
                f1.write("EMPTY")
                f2.write("EMPTY")
            else:    
                f1.write("# Incident particle energy (MeV) = \n# " + str(E_aRebin[i]/constants.physics.MeV_to_eV) + "\n#\n" +\
                        "# En.lab,MeV distribution\n")
                f2.write("# Incident particle energy (MeV) = \n# " + str(E_aRebin[i]/constants.physics.MeV_to_eV) + "\n#\n" +\
                        "# En.lab,MeV distribution\n")
                # for j in range(newFileLength): 
                #     f1.write(str("{:11.6f}".format(FIN_E_n[j]/constants.physics.MeV_to_eV)) + "  " + \
                #             str(FINdist[i,j]*constants.physics.MeV_to_eV) + "\n")   # перевод эВ->МэВ для сохранения нормировки
                for j in range(newArrayLength): 
                    f1.write(str("{:11.6f}".format(E_nRebin[j]/constants.physics.MeV_to_eV)) + "  " + \
                            str(distRebin[i,j]*constants.physics.MeV_to_eV) + "\n")   # перевод эВ->МэВ для сохранения нормировки
                    f2.write(str("{:11.6f}".format(E_nRebin[j]/constants.physics.MeV_to_eV)) + "  " + \
                            str(distRebin[i,j]*constants.physics.MeV_to_eV) + "\n")
            f1.close()
            f2.close()