#!/usr/bin/python
# -*- coding: utf-8 -*-

# Файл строит графики зависимости энергии вылетающего нйтрона от угла рассеяния для набора энергий налетающих альфа-частиц 

from __future__ import print_function
from __future__ import division
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import constants
import converter
import processor
import polynomials

def buildGraph(fname, MF, MT, points):
    
    while (True):
        if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)):  # проверка наличия директории
            processor.writeData(fname, int(MF), int(MT))
        
        counter = 1
        NK = 1  
        E_in = []
        A_i = [[]]
        if not os.path.isfile('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter+1)):
            break

        f = open('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter), 'w')
        lineNumber = 1
        for line in f.readlines():  # считываем построчно
            if (lineNumber == 6):
                E_in.append(float(line))
            if (lineNumber > 8):
                A_i[].append(float(line))
            B = processor.giveData(fname, MF=6, MT=50)

            print(B)
            l=len(B[:][0])
            print(a,l,'\n')
            
            A = polynomials.getLegendre(points,l)

            C = np.dot(A,B)
            print(C)


        counter += 1



