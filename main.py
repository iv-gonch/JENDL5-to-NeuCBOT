#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import sys
# import os

# import constants
# import chemistry
import converter
import processor
import adjuster
# import polynomials
import plotter

# ofile = sys.stdout


def main():   # как хотелось бы сделать
    # значения по умолчанию: 
    MT = int(50)        # тип реакции (см. манула ENDF6)
    points = int(101)   # количество точек в первичных функциях распределения
    dE_a = 1e4          # размер бина, eV
    dE_n = 1e5          # размер бина, eV

    for arg in sys.argv:
        if arg == '-MT':
            MT      = int(sys.argv[sys.argv.index(arg)+1])
        if arg == '-points':
            points  = int(sys.argv[sys.argv.index(arg)+1])
        if arg == '-dE_a':
            dE_a    = int(sys.argv[sys.argv.index(arg)+1])
        if arg == '-dE_n':
            dE_n    = int(sys.argv[sys.argv.index(arg)+1])
        if arg == '-nucleus':
            fname   = sys.argv[sys.argv.index(arg)+1]
            print('Inserting', fname, 'data into NeuCBOT.', file=sys.stdout)
            adjuster.neucbotIn(fname, MT, points, dE_a, dE_n)   # [dE_a] = [dE_n] = eV

    
# def main():

#     for arg in sys.argv:
        
#         # if arg == '-graph':
#         #     fname = sys.argv[sys.argv.index(arg)+1]
#         #     MF = int(sys.argv[sys.argv.index(arg)+2])
#         #     MT = int(sys.argv[sys.argv.index(arg)+3])
#         #     points = int(sys.argv[sys.argv.index(arg)+4])
#         #     dimension = sys.argv[sys.argv.index(arg)+5]
#         #     graphType = sys.argv[sys.argv.index(arg)+6]
#         #     if (dimension == '2D'):
#         #         print('Building 2D graphs of', points, 'points for', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
#         #         plotter.build2D(fname, MF, MT, points, graphType)                
#         #     if (dimension == '3D'):
#         #         print('Building 3D graph of', points, 'points for', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
#         #         plotter.build3D(fname, MF, MT, points, graphType)
        
#         if arg == '-convert':
#             fname = sys.argv[sys.argv.index(arg)+1]
#             print('Convreting file', fname, file=sys.stdout)
#             converter.convertENDF(fname)

#         if arg == '-reshape':
#             fname = sys.argv[sys.argv.index(arg)+1]
#             MF = int(sys.argv[sys.argv.index(arg)+2])
#             MT = int(sys.argv[sys.argv.index(arg)+3])
#             print('Reshaping data of', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
#             converter.separateData(fname, MF, MT)
        
#         if arg == '-spectra':
#             fname = sys.argv[sys.argv.index(arg)+1]
#             MF = int(sys.argv[sys.argv.index(arg)+2])
#             MT = int(sys.argv[sys.argv.index(arg)+3])
#             points = int(sys.argv[sys.argv.index(arg)+4])
#             print('Making sprctra data of', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
#             NK, NE, E_in, S, isData = processor.getEnergyAngleDistribtion(fname, MF, MT, points, normcheck = True)
#             processor.angle2spectrum(fname, MF, MT, points, NK, NE, E_in, S, isData)
        
#         if arg == '-adjust':
#             fname = sys.argv[sys.argv.index(arg)+1]
#             MF = int(sys.argv[sys.argv.index(arg)+2])
#             MT = int(sys.argv[sys.argv.index(arg)+3])
#             points = int(sys.argv[sys.argv.index(arg)+4])
#             dE_a = int(sys.argv[sys.argv.index(arg)+5])
#             print('Adjusting file', fname, file=sys.stdout)
#             adjuster.neucbotIn(fname, MT, points, dE_a, 1e5)   # [dE] = eV

if __name__ == '__main__':

    main()

# запускать bash script.sh 