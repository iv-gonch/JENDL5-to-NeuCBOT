#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import sys
import os

import constants
import converter
import processor
import polynomials
import plotter

# ofile = sys.stdout
    
def main():
    for arg in sys.argv:

        if arg == '-graph':
            fname = sys.argv[sys.argv.index(arg)+1]
            MF = sys.argv[sys.argv.index(arg)+2]
            MT = sys.argv[sys.argv.index(arg)+3]
            points = sys.argv[sys.argv.index(arg)+4]
            print('Building graph of', points, 'points for', fname, 'MF =', MF, 'MT =', MT, file=sys.stdout)
            plotter.buildGraph(fname, int(MF), int(MT), int(points))

        if arg == '-convert':
            fname = sys.argv[sys.argv.index(arg)+1]
            print('Convreting file', fname, file=sys.stdout)
            converter.convertENDF(fname)

        if arg == '-process':
            fname = sys.argv[sys.argv.index(arg)+1]
            MF = sys.argv[sys.argv.index(arg)+2]
            MT = sys.argv[sys.argv.index(arg)+3]
            print('Writing data for', fname, 'MF =', MF, 'MT =', MT, file=sys.stdout)
            processor.writeData(fname, int(MF), int(MT))

if __name__ == '__main__':
    main()

    # запускать bash script.sh 