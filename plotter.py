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


def build3D(fname, MF, MT, points, graphType):

    NK, NE, E_in, S, isData = processor.getEnergyAngleDistribtion(fname, MF, MT, points, check = True)

    if (isData):  # проверка на наличие данных для построения графика

        if (graphType == 'neutron_spectra'):
            
            elev=30.
            azim=15. 
            roll=0.
            
            cos_Theta, E_n, S, isData = processor.angle2spectrum(fname, MF, MT, points, )

            folderName = 'neutron spectra/'
            ylabel = 'En, cm E7*eV'
            zlabel = 'p_i(Ea, En)'
            ax = plt.figure().add_subplot(projection='3d')

            # a = np.zeros((NE, points+4), dtype=float)
            # y = np.zeros((NE, points+4), dtype=float)

            # # a = np.zeros((NE, points+2), dtype=float)
            # # y = np.zeros((NE, points+2), dtype=float)

            a = np.zeros((NE, points), dtype=float)
            y = np.zeros((NE, points), dtype=float)

            for i in range(NE):
                # a[i,0] = 0
                # a[i,1] = E_n[i,0]
                # a[i,-2] = E_n[i,-1]
                # a[i,-1] = np.max(E_in)

                # # a[i,0] = E_n[i,0]
                # # a[i,-1] = E_n[i,-1]

                SUMM = 0.
                SUMMCHECK = 0.

                for j in range(points-1):
                    SUMM += 0.5*(S[i,j] + S[i, j+1])*(E_n[i,j+1] - E_n[i,j])

                for j in range(points):
                    # a[i, j+2] = E_n[i,j]
                    # y[i, j+2] = S[i,j]

                    # # a[i, j+1] = E_n[i,j]
                    # # y[i, j+1] = S[i,j]

                    a[i,j] = E_n[i,j]
                    y[i,j] = S[i,j]
                    # y[i,j] = 1000000*S[i,j]/SUMM

                # if (E_in[i] >= 2500000):
                ax.plot(a[i], y[i], zs=E_in[i], zdir='x', color = 'black', linewidth = 0.5)

            if not os.path.isdir('graphs3D/'):  # проверка наличия директории
                os.mkdir('graphs3D/')    
            if not os.path.isdir('graphs3D/' + folderName):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName) 
            if not os.path.isdir('graphs3D/' + folderName + fname):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName + fname)
            if not os.path.isdir('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT))
            ax.view_init(elev, azim, roll)
            ax.text2D(0.05, 0.95, fname + ' MF' + str(MF) + ' MT' + str(MT), transform=ax.transAxes)
            ax.set_xlim(1.5e7, 0)    
            ax.set_ylim(0, np.max(a))
            ax.set_zlim(0, np.max(y))
            ax.set_xlabel('Ea, lab. E7*eV')
            ax.set_ylabel(ylabel)
            ax.set_zlabel(zlabel)
            
            plt.savefig('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_3D.png')

    
        if (graphType == 'angle_distribution'):

            elev=30.
            azim=30. 
            roll=0.

            folderName = 'angle distributions/'
            ylabel = 'cos(mu)'
            zlabel = 'p_i(Ea, mu)'
            ax = plt.figure().add_subplot(projection='3d')

            for i in range(NE):
                a = np.linspace(-1, 1, points)
                y = S[i]
                ax.plot(a, y, zs=E_in[i], zdir='x', color = 'black', linewidth = 0.5)

            if not os.path.isdir('graphs3D/'):  # проверка наличия директории
                os.mkdir('graphs3D/')    
            if not os.path.isdir('graphs3D/' + folderName):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName) 
            if not os.path.isdir('graphs3D/' + folderName + fname):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName + fname)
            if not os.path.isdir('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT))

            ax.text2D(0.05, 0.95, fname + ' MF' + str(MF) + ' MT' + str(MT), transform=ax.transAxes)
            ax.set_xlim(1.5e7, 0)   
            ax.set_ylim(np.min(a), np.max(a))
            ax.set_zlim(0, np.max(S))
            ax.set_xlabel('Ea, lab. E7*eV')
            ax.set_ylabel(ylabel)
            ax.set_zlabel(zlabel)
            ax.view_init(elev, azim, roll)
            plt.savefig('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_3D.png')


        if (graphType == 'kinematics'):

            cos_Theta, E_n, S, isData = processor.angle2spectrum(fname, MF, MT, points)

            folderName = 'kinematics/'
            ylabel = 'cos(mu)'
            zlabel = 'En, eV'
            ax = plt.figure().add_subplot(projection='3d')

            for i in range(NE):
                a = np.linspace(-1, 1, points)
                y = E_n[i]
                ax.plot(a, y, zs=E_in[i], zdir='x', color = 'black', linewidth = 0.5)

            if not os.path.isdir('graphs3D/'):  # проверка наличия директории
                os.mkdir('graphs3D/')    
            if not os.path.isdir('graphs3D/' + folderName):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName) 
            if not os.path.isdir('graphs3D/' + folderName + fname):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName + fname)
            if not os.path.isdir('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
                os.mkdir('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT))

            ax.text2D(0.05, 0.95, fname + ' MF' + str(MF) + ' MT' + str(MT), transform=ax.transAxes)
            ax.set_xlim(0, np.max(E_in))
            ax.set_ylim(-1., 1.)
            ax.set_zlim(0, np.max(E_n))
            ax.set_xlabel('Ea, eV')
            ax.set_ylabel(ylabel)
            ax.set_zlabel(zlabel)
            ax.view_init(elev, azim, roll)
            plt.savefig('graphs3D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_3D.png')


def build2D(fname, MF, MT, points, graphType):

    NK, NE, E_in, S, isData = processor.getEnergyAngleDistribtion(fname, MF, MT, points, check = True)

    if (isData):  # проверка на наличие данных для построения графика

        if (graphType == 'neutron_spectra'):

            cos_Theta, E_n, S, isData = processor.angle2spectrum(fname, MF, MT, points)

            folderName = 'neutron spectra/'

            a = np.zeros((NE, points+4), dtype=float)
            y = np.zeros((NE, points+4), dtype=float)

            for i in range(NE):
                a[i,0] = 0
                a[i,1] = E_n[i,0]
                a[i,-2] = E_n[i,-1]
                a[i,-1] = np.max(E_in)
                for j in range(points):
                    a[i, j+2] = E_n[i,j]
                    y[i, j+2] = S[i,j]

            if not os.path.isdir('graphs2D/'):  # проверка наличия директории
                os.mkdir('graphs2D/')    
            if not os.path.isdir('graphs2D/' + folderName):  # проверка наличия директории
                os.mkdir('graphs2D/' + folderName) 
            if not os.path.isdir('graphs2D/' + folderName + fname):  # проверка наличия директории
                os.mkdir('graphs2D/' + folderName + fname)
            if not os.path.isdir('graphs2D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
                os.mkdir('graphs2D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT))
            
            for i in range(NE):
                plt.axis([0, 15000000, 0, 1])
                # plt.axis([0, np.max(a), 0, np.max(y)])
                plt.title(fname + ' MF ' +  str(MF) + ' MT ' + str(MT) + ' E_in(alpha) = ' + str(E_in[i]*(10**(-6))) + ' MeV', fontsize=10)
                plt.xlabel('E_n, eV', color='black')
                plt.ylabel('Neutron yield', color='black')
                plt.grid(True)
                plt.plot(a[i],y[i], 'r-')
                plt.savefig('graphs2D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(i+1) + '.png')
                plt.clf()

            all_in_one_plot = 0

            if (all_in_one_plot):

                a = np.zeros((NE, points), dtype=float)
                y = np.zeros((NE, points), dtype=float)

                for i in range(NE):
                    for j in range(points):
                        a[i, j] = E_n[i,j]
                        y[i, j] = S[i,j]

                if not os.path.isdir('graphs2D/'):  # проверка наличия директории
                    os.mkdir('graphs2D/')    
                if not os.path.isdir('graphs2D/' + folderName):  # проверка наличия директории
                    os.mkdir('graphs2D/' + folderName) 
                if not os.path.isdir('graphs2D/' + folderName + fname):  # проверка наличия директории
                    os.mkdir('graphs2D/' + folderName + fname)
                if not os.path.isdir('graphs2D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT)):  # проверка наличия директории
                    os.mkdir('graphs2D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT))
                
                plt.axis([0, np.max(a), 0, np.max(y)])
                plt.title(fname + ' MF ' +  str(MF) + ' MT ' + str(MT) + ' E_in(alpha) from 0 to ' + str(E_in[i]*(10**(-6))) + ' MeV', fontsize=10)
                plt.xlabel('E_n, eV', color='gray')
                plt.ylabel('Neutron yield', color='gray')
                plt.grid(True)

                legenda = ['']*(NE//10)
                # for i in range(NE):
                for i in range(NE//10): # для каждой энергии
                    # plt.plot(a[i],y[i], 'r-')
                    plt.plot(a[i*10],y[i*10], '-', color=(1./(0.5*i+1), 1./(NE//10 - i+1), 1./(NE//10 - i+1))) #, linewidth = 0.5
                    plt.savefig('graphs2D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(i+1) + '.png')
                    legenda[i] = 'Ea = ' + str(E_in[i*10]*(10**(-6))) + ' MeV'
                plt.legend(legenda)
                plt.savefig('graphs2D/' + folderName + fname + '/MF' +  str(MF) + '_MT' + str(MT) + '_NK.png')
                plt.clf()
