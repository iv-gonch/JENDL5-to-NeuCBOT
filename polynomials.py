#!/usr/bin/python
# -*- coding: utf-8 -*-

# Возвращает двумерный numpy массив размерности [axl], где 'a' - число значений на интервале [-1; 1] с равными промежутками 
# и 'l' - число вычисленных полиномов Лежандра
# Массив содержит значения каждого из 'l' полиномов Лежандра в каждой из 'a' точек интервала [-1; 1] 

from __future__ import print_function
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import os
import constants

def getLegendre(a, l):  # a - количество точек по косинусу угла (от -1 до 1), 
                        # l - количество коэффициентов Лежандра (NW часто = NL. NL это l)

    P = np.ones((a, l), dtype = float) # создаём двумерный массив размерности [a]x[l]
        # P[:][0] = 1.    # задаём два первых члена для рекуррентной формулы 
        # P[:][1] = x     # P(n+1,x) = (2*n+1)/(n+1)*x*P(n,x) - n/(n+1)*P(n-1,x)

    # область ортогональности плиномов Лежандра лежит от -1 до 1 (бывают сдвинутые, когда от 0 до 1)
    x = np.linspace(-1, 1, a)  # "х" задаём так, чтобы он прошёл за "a" шагов от -1 до 1 включительно 
    P[:,1] = [x[i] for i in range(a)]  # задаём первый член полинома = х (нулевой и так уже = 1.)   
    for j in range(l-2): 
        # P(n+1,x) = (2*n+1)/(n+1)*x*P(n,x) - n/(n+1)*P(n-1,x)
        P[:,j+2] = ((2*j+3)*x*P[:,j+1] - (j+1)*P[:,j])/(j+2) # рекуррентная формула та же, но вместо n подставленно n+1



    # if not os.path.isdir('graphs2D/'):  # проверка полиномов Лежандра
    #     os.mkdir('graphs2D/')  
    # if not os.path.isdir('graphs2D/legendre/'): 
    #     os.mkdir('graphs2D/legendre/')    

    # for j in range(l):
    #     plt.axis([-1.05,1.05,-1.05,1.05])
    #     plt.title('l = ' + str(j), fontsize=10)
    #     plt.grid(True)
    #     plt.plot(x, P[:,j], color=(1, .0, 0.0))
    #     plt.savefig('graphs2D/legendre/l_' + str(j) + '.png')
    #     plt.clf()
    # # plt.savefig('graphs2D/legendre/l.png')
    # # plt.clf()



    return P