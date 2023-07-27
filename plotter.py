#!/usr/bin/python
# -*- coding: utf-8 -*-

# Файл строит графики зависимости энергии вылетающего нйтрона от угла рассеяния для набора энергий налетающих альфа-частиц 

from __future__ import print_function
from __future__ import division
import sys
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

import constants
import converter
import processor
import polynomials


def build3D(fname, MF, MT, NK, NE, points, S, E_in):

    if not os.path.isdir('graphs/'):  # проверка наличия директории
        os.mkdir('graphs/')    
    
    if not os.path.isdir('graphs/' + str(fname)):  # проверка наличия директории
        os.mkdir('graphs/' + str(fname))


    if not os.path.isdir('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
        os.mkdir('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT))

    ax = plt.figure().add_subplot(projection='3d')

    # Plot a sin curve using the x and y axes.
    # for i in range(NE):
    #     x = E_in[i]
    #     y = np.linspace(-1, 1, points)
    #     ax.plot(x, y, zs=S[i], zdir='z', label='curve in (z, y)')
    for i in range(NE):
        a = np.linspace(-1, 1, points)
        y = S[i]
        ax.plot(a, y, zs=E_in[i], zdir='x', label=' (x, y)', color = 'black', linewidth = 0.5)

    # ax.legend()

    ax.set_xlim(np.min(E_in), np.amax(E_in))    
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, np.amax(S)*1.2)

    ax.set_xlabel('E_in, eV')
    ax.set_ylabel('cos(mu)')
    ax.set_zlabel('p_i(E_in, mu)')
    
    ax.view_init(elev=20., azim=195, roll=0)

    plt.savefig('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_3D.png')

def build2D(NE, S, fname, MF, MT, E_in, points, NK):

    if not os.path.isdir('graphs/'):  # проверка наличия директории
        os.mkdir('graphs/')    
    
    if not os.path.isdir('graphs/' + str(fname)):  # проверка наличия директории
        os.mkdir('graphs/' + str(fname))


    if not os.path.isdir('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
        os.mkdir('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT))

    for i in range(NE): # для каждой энергии
        plt.axis([-1,1,0,np.amax(S)*1.2])
        plt.title(fname + ' MF ' +  str(MF) + ' MT ' + str(MT) + ' E_in(alpha) = ' + str(E_in[i]/10*(-6)) + ' MeV', fontsize=10)
        plt.xlabel('Cosine of emmition angle', color='gray')
        plt.ylabel('Normalizeg neutron yield', color='gray')
        plt.grid(True)
        plt.plot(np.linspace(-1, 1, points),S[i],'r-')
        plt.savefig('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(i+1) + '.png')
        plt.clf()


def buildGraph(fname, MF, MT, points, dimension):
    
    NK = 1  # есть в названии директории. Отвечает за количество различных вылетющих частц
    counter = 1 # счётчик по эенргии
    E_in = []   # массив энергий налетающих альфа частиц
    Coeff = []  # двумерный массив коэффициентов Лежандра
    
#========= считываем файлы в массивы =========#

    if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)):  # проверка наличия директории
        processor.writeData(fname, int(MF), int(MT))

    while (True):   # пока не закончатся файлы в директории /processed/fname/MF**_MT***/
        if not os.path.isfile('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter)):
            # когда прошли все E_in для нынешнего NK
            if os.path.isfile('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter)):  
                NK += 1
                print(fname, 'MF', MF, 'MT', MT, 'contains data of more than one product particle') # проверка количества вылетающих частиц
            else:
                break   # остановиться когда прошли все NK и E_in 

        f = open('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter), 'r')
        NS = 0  # номер строки в файле
        for line in f.readlines():  # считываем построчно
            if (NS == 5):   # строка, где записана энергия влетающей альфа-частицы
                E_in.append(float(line))    # записываем энергию альфа частицы
                Coeff.append([])    # создаём место для записи коэффициентов Лежандра
            if (NS > 7 and line != ''):    # строки, где хранятся коэффициенты Лежандра 
                Coeff[counter-1].append(float(line))
            NS += 1
        counter += 1

#========= вычисляем углы из Лежандра =========#

    maxNW = len(max(Coeff[:], key=len))  # максимальное количество чисел в файле
    NE = len(Coeff) # число различных энергий налетающей альфа-частицы 
    
    A = np.zeros((NE, maxNW), dtype = float)    # массив коэффициентов Лежандра
    P = polynomials.getLegendre(points,maxNW + 1)   # массив значений полиномов Лежандра в точках 
        # (+1 нужен тк нулеввой член полинома не участвует в формуле из мануала) 
    C = np.zeros((points, maxNW), dtype = float)# массив произведения A*P для каждой энергии и для каждой точки 
    S = np.zeros((NE, points), dtype = float)
    
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

#============ проверка вычислений ============# 0.15202460931963135 - самое обольшое отклонение от 1.0 для C12 MF6 MT50

        SUMMCHECK = 0.0   # проверка нормировки p_i (mu,E_in) (в мануале сказано, что эта функция нормированна)
        for j in range(points): # для каждой точки
            SUMMCHECK += S[i,j]*2/(points-1)
        if (abs(SUMMCHECK - 1) > 0.1):
            print('Warning! This number ' + str(SUMMCHECK) + ' must be equal 1.0\nCheck plotter.py')

#============ строим кучу двумерных графиков ============#  NE, S, fname, MF, MT, E_in, points, NK,
    if (dimension == 2):
        build2D(NE, S, fname, MF, MT, E_in, points, NK)

#============ строим трёхмерный графк ============#
    if (dimension == 3):
        build3D(fname, MF, MT, NK, NE, points, S, E_in)