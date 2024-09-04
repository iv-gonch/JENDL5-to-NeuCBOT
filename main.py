#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import sys

import adjuster


def main():   # как хотелось бы сделать
    # значения по умолчанию: 
    fname = ""
    MT = int(50)        # тип реакции (см. манула ENDF6)
    points = int(101)   # количество точек в первичных функциях распределения
    dE_a = 1e4          # размер бина, eV
    dE_n = 1e5          # размер бина, eV

    for arg in sys.argv:
        if arg == "-MT":
            MT      = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "-points":
            points  = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "-dE_a":
            dE_a    = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "-dE_n":
            dE_n    = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "-nucleus":
            fname   = sys.argv[sys.argv.index(arg)+1]
            print("Trying to insert into NeuCBOT " + fname + " data for (a,n" + str(MT-50) + ")-reaction.", file=sys.stdout)
            adjuster.neucbotIn(fname, MT, points, dE_a, dE_n)   # [dE_a] = [dE_n] = eV
    if not (fname):
        print("You need to set the element. \nAdd line \"-nucleus C_13\" after main.py")
    else:
        print("JENDL-based data for " + fname + " is stored now in ./stage_2_data and ../neucbot/Data/Isotopes/" + \
                     fname.split("_")[0] + "/" + fname.replace("_", "") + "/JendlOut")
    

if __name__ == "__main__":

    main()

# запускать bash script.sh 