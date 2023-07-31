#!/usr/bin/python
# -*- coding: utf-8 -*-

# Считывает строки с конкретными MF и MT из конвертированного файла. 
# Записывает в папку /reshaped/filename/MF**_MT***/NK**_NE*** функцию p_i(theta) для каждой энергии налетающей альфа частицы

from __future__ import print_function
from __future__ import division
import numpy as np
import math
import sys
import os

import plotter
import constants
import chemistry
import converter
import polynomials


def legendre2angle(Coeff, points, NE):

    maxNW = len(max(Coeff[:], key=len)) # максимальное количество чисел в файле
    A = np.zeros((NE, maxNW), dtype = float)    # массив коэффициентов Лежандра
    P = polynomials.getLegendre(points,maxNW + 1)   # массив значений полиномов Лежандра в точках 
        # (+1 нужен тк нулеввой член полинома не участвует в формуле из мануала) 
    C = np.zeros((points, maxNW), dtype = float)# массив произведения A*P для каждой энергии и для каждой точки 
    S = np.zeros((NE, points), dtype = float)   # массив значений выхода в точках

    for i in range(NE): # для каждой энергии
        NW = len(Coeff[i])
        S[i,:] = 0.5

        for j in range(NW): 
            A[i,j] = Coeff[i][j]    # A[NE, l]

        for j in range(points): # для каждой точки
            for k in range(maxNW):
                C[j, k] = P[j,k+1] * A[i,k] * (2*(k+1) + 1)/2
                # (k+1 нужен тк так было в формуле из мануала) 
                S[i,j] += C[j,k]

    return S


def normCheck(NE, points, S):

    for i in range(NE):
        SUMMCHECK = 0.0   # проверка нормировки p_i (mu,E_in) (в мануале сказано, что эта функция нормированна)

        for j in range(points): # для каждой точки
            SUMMCHECK += S[i,j]*2/(points-1)

        if (abs(SUMMCHECK - 1) > 0.1):
            print('Warning! This number ' + str(SUMMCHECK) + ' must be equal 1.0\nCheck processor.getEnergyAngleDistribtion()')


def getEnergyAngleDistribtion(fname, MF, MT, points, check):
    
    NK = 1  # есть в названии директории. Отвечает за количество различных вылетющих частц
    counter = 1 # счётчик по эенргии
    E_in = []   # массив энергий налетающих альфа частиц
    Coeff = []  # будущий двумерный массив коэффициентов Лежандра

#========= сохраняем данный из файлов в массивы E_in, Coeff,=========#

    if not os.path.isdir('reshaped/' + fname + '/MF' + str(MF) + '_MT' + str(MT)):  # проверка наличия директории
        converter.separateData(fname, int(MF), int(MT))

    while (True):   # пока не закончатся файлы в директории /reshaped/fname/MF**_MT***/
        
        if not os.path.isfile('reshaped/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter)):    # на будущее, когда будет несколько вылетающих частиц
            # когда прошли все E_in для нынешнего NK
            if os.path.isfile('reshaped/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter)):  
                NK += 1
                print(fname, 'MF', MF, 'MT', MT, 'contains data of more than one product particle') # проверка количества вылетающих частиц
            else:
                break   # остановиться когда прошли все NK и E_in 

        f = open('reshaped/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter), 'r')
        NS = 0  # номер строки в файле
        
        for line in f.readlines():  # считываем построчно
            if (NS == 6):   # строка, где записана энергия влетающей альфа-частицы
                E_in.append(float(line))    # записываем энергию альфа частицы
                Coeff.append([])    # создаём место для записи коэффициентов Лежандра

            if (NS > 8 and line != ''):    # строки, где хранятся коэффициенты Лежандра 
                Coeff[counter-1].append(float(line))

            NS += 1

        counter += 1

#========= вычисляем и записываем значение угла (через коэффициенты Лежандра) =========#

    if (len(Coeff[:]) == 0):    #  если в файле нет данных 
        print('\n' + fname, 'MF'+ str(MF), 'MT' + str(MT), 'has no Legenge coefficients!\n')
        NK, NE, E_in, S, isData = 0, 0, [], [], False

    else:
        NE = len(Coeff) # число различных энергий налетающей альфа-частицы 
        S = legendre2angle(Coeff, points, NE)   # вычисляем углы из Лежандра 
        isData = True
        
#============ проверка вычислений ============# 0.15202460931963135 - самое обольшое отклонение от 1.0 для C12 MF6 MT50
        if check:
            normCheck(NE, points, S)

#============ выводим кортеж значений для графиков ============# 

    return NK, NE, E_in, S, isData  # можно не возвращать NE тк это длина E_in. Но надо переписать много где


def angle2spectrum(fname, MF, MT, points):# из распределения theta_neutron(E_alpha) получаем зависимость E_neutron(E_alpha) по кинематической формуле без учёта релятивизма
    
    NK, NE, E_in, S, isData = getEnergyAngleDistribtion(fname, MF, MT, points, check = False)

    if (isData):  # проверка на наличие данных для вычисления спектра

        ele = fname.split('_')[0]
        Z = int(chemistry.getZ(ele))
        A = int(fname.split('_')[1])

        ZA_in = Z*1000 + A
        mass_in = chemistry.getMass(ZA_in)

        mass_a = chemistry.getMass(2004)

        ZA_out = (Z+2)*1000 + (A+1)
        mass_out = chemistry.getMass(ZA_out)

        mass_n = chemistry.getMass(1)

        Q = mass_in + mass_a - mass_out - mass_n

        E_n = np.zeros(points)
        E_a = np.zeros(NE)
        cos_THeta = np.linspace(-1, 1, points)

        for i in range(NE): # для каждой энергии
            E_a[i] = E_in[i]

            longLine = mass_a*mass_n*E_in[i] * (mass_n + mass_out) * (mass_a*E_in[i] - mass_out*Q - mass_out*E_in[i])

            for j in range(points): 
                E_n[i] = (2*mass_a*mass_n*E_a[i]*cos_THeta[j]**2 - longLine + 2*cos_THeta[j] * np.sqrt( (mass_a*mass_n*E_a[i]*cos_THeta[j])**2 - longLine))/(mass_n + mass_out)**2