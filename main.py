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
# import polynomials
import plotter

# ofile = sys.stdout

    
def main():

    for arg in sys.argv:
        
        if arg == '-graph':
            fname = sys.argv[sys.argv.index(arg)+1]
            MF = int(sys.argv[sys.argv.index(arg)+2])
            MT = int(sys.argv[sys.argv.index(arg)+3])
            points = int(sys.argv[sys.argv.index(arg)+4])
            dimension = sys.argv[sys.argv.index(arg)+5]
            graphType = sys.argv[sys.argv.index(arg)+6]
            if (dimension == '2D'):
                print('Building 2D graphs of', points, 'points for', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
                plotter.build2D(fname, MF, MT, points, graphType)                
            if (dimension == '3D'):
                print('Building 3D graph of', points, 'points for', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
                plotter.build3D(fname, MF, MT, points, graphType)
        
        if arg == '-convert':
            fname = sys.argv[sys.argv.index(arg)+1]
            print('Convreting file', fname, file=sys.stdout)
            converter.convertENDF(fname)

        if arg == '-reshape':
            fname = sys.argv[sys.argv.index(arg)+1]
            MF = int(sys.argv[sys.argv.index(arg)+2])
            MT = int(sys.argv[sys.argv.index(arg)+3])
            print('Reshaping data of', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
            converter.separateData(fname, MF, MT)
        
        if arg == '-spectra':
            fname = sys.argv[sys.argv.index(arg)+1]
            MF = int(sys.argv[sys.argv.index(arg)+2])
            MT = int(sys.argv[sys.argv.index(arg)+3])
            points = int(sys.argv[sys.argv.index(arg)+4])
            print('Making sprctra data of', fname, 'MF'+ str(MF), 'MT' + str(MT), file=sys.stdout)
            NK, NE, E_in, S, isData = processor.getEnergyAngleDistribtion(fname, MF, MT, points, normcheck = True)
            processor.angle2spectrum(fname, MF, MT, points, NK, NE, E_in, S, isData)

if __name__ == '__main__':

    main()

    # запускать bash script.sh 