#!/usr/bin/python
# -*- coding: utf-8 -*-

# Файл вычисляет 'a' значений для первых 'l' членов полинома Лежандра на интервале [-1; 1] с равными промежутками

from __future__ import print_function
from __future__ import division
import numpy as np
import math
import sys
import os
import constants

def getLegendre(a, l):   # a - количество точек по косинусу угла (от -1 до 1), 
                            # l - количество коэффициентов Лежандра (NW часто = NL. NL это l)

    P = np.ones((a, l), dtype = float) # создаём двумерный массив размерности [a]x[l]
        # P[:][0] = 1.    # задаём два первых члена для рекуррентной формулы 
        # P[:][1] = x     # P(n+1,x) = (2*n+1)/(n+1)*x*P(n,x) - n/(n+1)*P(n-1,x)

    # область ортогональности плиномов Лежандра лежит от -1 до 1 (бывают сдвинутые, когда от 0 до 1)
    x = np.linspace(-1, 1, a)  # "х" задаём так, чтобы он прошёл за "a" шагов от -1 до 1 включительно 

    P[:][1] = [x[i] for i in range(a)]  # задаём первый член полинома = х (нулевой и так уже = 1.)   
    for j in range(l-2): 
        # P(n+1,x) = (2*n+1)/(n+1)*x*P(n,x) - n/(n+1)*P(n-1,x)
        P[:][j+2] = (2*j+3)/(j+2)*x*P[:][j+1] - (j+1)/(j+2)*P[:][j] # рекуррентная формула та же, но вместо n подставленно n+1
        
    # for : in range(0, len(P)):
    #     for i2 in range(0, len(P[:])):
    #         print(P[:][i2], end='\t')
    #     print()

    return P