#!/usr/bin/python
# -*- coding: utf-8 -*-

# Файл строит графики зависимости энергии вылетающего нйтрона от угла рассеяния для набора энергий налетающих альфа-частиц 

from __future__ import print_function
from __future__ import division
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

import constants
import converter
import processor
import polynomials


def build3D(fname, MF, MT, points):

    NK, NE, E_in, S, isData = processor.getEnergyAngleDistribtion(fname, MF, MT, points, check = True)

    if (isData):  # проверка на наличие данных для построения графика

        if not os.path.isdir('graphs/'):  # проверка наличия директории
            os.mkdir('graphs/')    
        if not os.path.isdir('graphs/' + str(fname)):  # проверка наличия директории
            os.mkdir('graphs/' + str(fname))
        if not os.path.isdir('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
            os.mkdir('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT))

        ax = plt.figure().add_subplot(projection='3d')

        for i in range(NE):
            a = np.linspace(-1, 1, points)
            y = S[i]
            ax.plot(a, y, zs=E_in[i], zdir='x', label=' (x, y)', color = 'black', linewidth = 0.5)
            
        ax.text2D(0.05, 0.95, fname + ' MF' + str(MF) + ' MT' + str(MT), transform=ax.transAxes)
        ax.set_xlim(np.min(E_in), np.amax(E_in))    
        ax.set_ylim(-1, 1)
        ax.set_zlim(0, np.amax(S)*1.2)
        ax.set_xlabel('E_in, eV')
        ax.set_ylabel('cos(mu)')
        ax.set_zlabel('p_i(E_in, mu)')
        ax.view_init(elev=20., azim=195, roll=0)
        plt.savefig('graphs/' + str(fname) + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_3D.png')


def build2D(fname, MF, MT, points):

    NK, NE, E_in, S, isData = processor.getEnergyAngleDistribtion(fname, MF, MT, points, check = True)

    if (isData):  # проверка на наличие данных для построения графика

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
