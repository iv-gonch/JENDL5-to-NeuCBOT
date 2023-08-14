#!/usr/bin/python
# -*- coding: utf-8 -*-

# Возвращает двумерный numpy массив размерности [axl], где 'points' - число значений на интервале [-1; 1] с равными промежутками 
# и 'lmax' - число вычисленных полиномов Лежандра
# Массив содержит значения каждого из 'lmax' полиномов Лежандра в каждой из 'points' точек интервала [-1; 1] 

from __future__ import print_function
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import os
import constants


def getLegendre(points, lmax):  # points - количество точек по косинусу угла (от -1 до 1), 
                        # lmax - количество коэффициентов Лежандра (NW часто = NL. NL это lmax)

    P = np.ones((points, lmax), dtype = float) # создаём двумерный массив размерности [points]x[lmax]
        # P[:][0] = 1.    # задаём два первых члена для рекуррентной формулы 
        # P[:][1] = x     # P(n+1,x) = (2*n+1)/(n+1)*x*P(n,x) - n/(n+1)*P(n-1,x)

    # область ортогональности плиномов Лежандра лежит от -1 до 1 (бывают сдвинутые, когда от 0 до 1)
    x = np.linspace(-1, 1, points)  # "х" задаём так, чтобы он прошёл за "points" шагов от -1 до 1 включительно 
    P[:,1] = [x[i] for i in range(points)]  # задаём первый член полинома = х (нулевой и так уже = 1.)   
    for l in range(lmax-2): 
        # P(n+1,x) = (2*n+1)/(n+1)*x*P(n,x) - n/(n+1)*P(n-1,x)
        P[:,l+2] = ((2*l+3)*x*P[:,l+1] - (l+1)*P[:,l])/(l+2) # рекуррентная формула та же, но вместо n подставленно n+1



    # if not os.path.isdir('graphs2D/'):  # проверка полиномов Лежандра
    #     os.mkdir('graphs2D/')  
    # if not os.path.isdir('graphs2D/legendre/'): 
    #     os.mkdir('graphs2D/legendre/')    

    # for l in range(lmax):
    #     plt.axis([-1.05,1.05,-1.05,1.05])
    #     plt.title('lmax = ' + str(l), fontsize=10)
    #     plt.grid(True)
    #     plt.plot(x, P[:,l], color=(1, .0, 0.0))
    #     plt.savefig('graphs2D/legendre/l_' + str(l) + '.png')
    #     plt.clf()
    # # plt.savefig('graphs2D/legendre/lmax.png')
    # # plt.clf()



    return P