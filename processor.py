#!/usr/bin/python
# -*- coding: utf-8 -*-

# Считывает строки с конкретными MF и MT из конвертированного файла. 
# Записывает в папку /reshaped/filename/MF**_MT***/NK**_NE*** функцию p_i(theta) для каждой энергии налетающей альфа частицы

from __future__ import print_function
from __future__ import division
import numpy as np
import math
# import sys
import os

# import plotter
# import constants
import chemistry
import converter
import polynomials


def normCheck(NE, points, dist, fname):

    for i in range(NE):
        SUMMCHECK = 0.0   # проверка нормировки p_i (mu,E_in) (в мануале сказано, что эта функция нормированна)
        for j in range(points-1): # для каждой точки
            SUMMCHECK += (dist[i,j] + dist[i,j+1])/2 * 2./(points-1)
        if (abs(SUMMCHECK - 1) > 1.e-2):
            print("Warning! This number " + str(SUMMCHECK - 1.)  + " must be equal 0.0 for " + fname + ". NE = " + str(i) + "\nCheck processor.getEnergyAngleDistribtion()")


def legendre2angle(Coeff, points, NE):  # из коэффициентов лежандра получаем значения функции распределения по cos(theta)

    maxNW = len(max(Coeff[:], key=len)) # максимальное количество чисел в файле

    A = np.zeros((NE, maxNW+1), dtype = float)    # массив коэффициентов Лежандра
    P = polynomials.getLegendre(points,maxNW + 1)   # массив значений полиномов Лежандра в точках 
        # (+1 нужен тк нулеввой член полинома не участвует в формуле из мануала) 
    dist_angle = np.ones((NE, points), dtype = float)   # массив значений выхода в точках. В мауале это p_i[E_in, cos(mu)]
    dist_angle /= 2.

    for i in range(NE): # для каждой энергии
        NW = len(Coeff[i])

        for j in range(NW): 
            A[i,j] = Coeff[i][j]    # A[NE, l] просто ради массива numpy
        for j in range(points): # для каждой точки
            for l in range(maxNW):
                dist_angle[i,j] += P[j,l+1] * A[i,l] * (2.*(l+1.) + 1.)/2.     # (l+1 нужен тк в формуле из мануала сумма начинается с l = 1) 
    return dist_angle


def getEnergyAngleDistribtion(fname, MT, points, normcheck):
    NK = 1  # есть в названии директории. Отвечает за количество различных вылетющих частц
    counter = 0 # счётчик по эенргии
    E_in = []   # массив энергий налетающих альфа частиц
    Coeff = []  # будущий двумерный массив коэффициентов Лежандра

#========= сохраняем данный из файлов в массивы E_in, Coeff,=========#

    if not os.path.isdir("reshaped/" + fname + "/MF6_MT" + str(MT)):  # проверка наличия директории
        converter.separateData(fname, MT)

    while (True):   # пока не закончатся файлы в директории /reshaped/fname/MF**_MT***/
        if not os.path.isfile("reshaped/" + fname + "/MF6_MT" + str(MT) + "/NK" + str(NK) + "_NE" + str(counter)):    # на будущее, когда будет несколько вылетающих частиц
            # когда прошли все E_in для нынешнего NK
            if os.path.isfile("reshaped/" + fname + "/MF6_MT" + str(MT) + "/NK" + str(NK) + "_NE" + str(counter)):  
                NK += 1
                print(fname, "MF = 6 MT =", MT, "contains data of more than one product particle") # проверка количества вылетающих частиц
            else:
                break   # остановиться когда прошли все NK и E_in 

        f = open("reshaped/" + fname + "/MF6_MT" + str(MT) + "/NK" + str(NK) + "_NE" + str(counter), "r")
        NS = 0  # номер строки в файле
        
        for line in f.readlines():  # считываем построчно
            if (NS == 6):   # строка, где записана энергия влетающей альфа-частицы
                E_in.append(float(line))    # записываем энергию альфа частицы
                Coeff.append([])    # создаём место для записи коэффициентов Лежандра
            if (NS > 8 and line != ""):    # строки, где хранятся коэффициенты Лежандра 
                Coeff[counter].append(float(line))
            NS += 1
        counter += 1
        f.close()

#========= вычисляем и записываем значение угла (через коэффициенты Лежандра) =========#

    if (len(Coeff[:]) == 0):    #  если в файле нет данных 
        print(fname, "MF 6 MT" + str(MT), "has no Legendre coefficients!")
        NK, NE, E_in, dist_angle, isData = 0, 0, [], [], False
    else:
        NE = len(Coeff) # число различных энергий налетающей альфа-частицы 
        dist_angle = legendre2angle(Coeff, points, NE)   # вычисляем углы из Лежандра 
        isData = True
        
#============ проверка вычислений ============# самое обольшое отклонение от 1.0, которое я видел, было у C12 MF6 MT50
        
        if normcheck:
            normCheck(NE, points, dist_angle, fname)

#============ выводим кортеж значений для графиков ============# 

    return NK, NE, E_in, dist_angle, isData  # можно не возвращать NE тк это длина E_in. Но это надо исправлять везде, где вызывается функция


def angle2spectrum(fname, MT, points, NK, NE, E_in, dist_angle, isData):# из распределения theta_neutron(E_alpha) получаем зависимость E_neutron(E_alpha) по кинематической формуле без учёта релятивизма
    MF = int(6)
    if (isData):  # проверка на наличие данных для вычисления спектра

        if not os.path.isdir("angle_distribution"):  # проверка наличия директории
            os.mkdir("angle_distribution")
        if not os.path.isdir("angle_distribution/" + fname): # проверка наличия директории
            os.mkdir("angle_distribution/" + fname)
        if not os.path.isdir("angle_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT)): # проверка наличия директории
            os.mkdir("angle_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT))

        if not os.path.isdir("En_distribution"):  # проверка наличия директории
            os.mkdir("En_distribution")
        if not os.path.isdir("En_distribution/" + fname): # проверка наличия директории
            os.mkdir("En_distribution/" + fname)
        if not os.path.isdir("En_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT)): # проверка наличия директории
            os.mkdir("En_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT))

        ele = fname.split("_")[0]
        Z = int(chemistry.getZ(ele))
        A = int(fname.split("_")[1])

        ZA_in = Z*1000 + A  
        In = chemistry.getMass(ZA_in)

        ZA_out = (Z+2)*1000 + (A+3)
        Out = chemistry.getMass(ZA_out)

        a = chemistry.getMass(2004) # в эВ
        n = chemistry.getMass(1)    # в эВ

        Q = In + a - Out - n    # в эВ

        E_n = np.zeros((NE, points), dtype=float)
        E_a = np.zeros(NE, dtype=float)
        cos_Theta = np.linspace(-1, 1, points)

        dist_En = np.zeros_like(dist_angle)

        for i in range(NE): # для каждой энергии
            f1 = open("angle_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT) + \
                      "/NK" + str(NK) + "_NE" + str(i), "w")
            f2 = open("En_distribution/" + fname + "/MF" + str(MF) + "_MT" + str(MT) + \
                      "/NK" + str(NK) + "_NE" + str(i), "w")
            
            E_a[i] = E_in[i]    # в эВ

            f1.write("Incident particle energy (eV) = \n" + str(E_a[i]) + "\n\n" + \
                     "cos(theta) distribution \n")
            f2.write("Incident particle energy (eV) = \n" + str(E_a[i]) + "\n\n" + \
                     "E_n lab,eV distribution \n")

            longLine = (n+Out) * (Out*(Q+E_a[i]) - a*E_a[i])    # изначально было

            E_treshold_lab = 0.
            if (Q < 0):
                E_treshold_lab = -Q*(1. + a/In - Q/(2.*In)) # в эВ
            if (E_a[i] < E_treshold_lab):
                print (E_a[i], "= E_a < E_treshold =", E_treshold_lab)
                continue
            for j in range(points): 
                shortLine = 2.* a * E_a[i] * n * cos_Theta[j]**2.   

                if (shortLine**2.+ 2.*shortLine*longLine < 0):
                    print(Q+E_a[i])

                if (cos_Theta[j] > 0.):
                    E_n[i,j] = (shortLine+longLine + np.sqrt(shortLine**2.+ 2.*shortLine*longLine)) / (n+Out)**2.
                else:
                    E_n[i,j] = (shortLine+longLine - np.sqrt(shortLine**2.+ 2.*shortLine*longLine)) / (n+Out)**2. 
                    
                dist_En[i,j] = dist_angle[i,j] * \
                    (((a+Out)/np.sqrt(16*n*E_n[i,j]*a*E_a[i])) + \
                     (((n+Out)*(Out*(Q+E_a[i])-a*E_a[i]))/\
                      (4*(a+Out)*np.sqrt(E_n[i,j]**3*n*a*E_a[i]))))   # f(mu) * d mu = f(En) * (d mu / d En) dEn

                f1.write(str("{:10.7f}".format(cos_Theta[j])) + " " + \
                         str("{:12.10f}".format(dist_angle[i,j])) + "\n")
                f2.write(str("{:10.1f}".format(E_n[i,j])) + " " + \
                         str("{:e}".format(dist_En[i,j])) + "\n")
            
            f1.close()
            f2.close()
        return cos_Theta, E_n, dist_En, isData