# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import sys
import subprocess

import converter
import processor
import adjuster

# Add 91 for continuum energy level 
MT_list =  {"Li_6" : [4, 50, 51, 52, 53],
            "Li_7" : [4, 50, 51, 52, 53, 54], 
            "Be_9" : [4, 50, 51, 52], 
            "B_10" : [4, 50, 51, 52, 53, 54], 
            "B_11" : [4, 50, 51, 52, 53, 54], 
            "C_12" : [4, 50], 
            "C_13" : [4, 50, 51, 52, 53, 54], 
            "N_14" : [4, 50, 51, 52, 53, 54], 
            "N_15" : [4, 50, 51, 52, 53, 54], 
            "O_17" : [4, 50, 51, 52, 53], 
            "O_18" : [4, 50, 51, 52, 53, 54], 
            "F_19" : [4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], 
            "Na_23": [4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]}  

def main(): 
    # значения по умолчанию: 
    recalculate_flag = False
    fname = ""
    # MT = int(50)        # тип реакции (см. мануал ENDF6)
    points = int(101)   # количество точек в первичных функциях распределения
    dE_a = 1e4          # размер бина по энергии альфа-частицы, eV
    dE_n = 1e5          # размер бина по энергии нейтрона, eV
    
    for arg in sys.argv:
        # if arg == "-MT":
            # MT      = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "--points":
            points = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "--dE_a":
            dE_a   = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "--dE_n":
            dE_n   = int(sys.argv[sys.argv.index(arg)+1])
        if arg == "--recalculate":
            recalculate_flag = True
            # Скачиваем JENDL-5 Alpha-particle sublibrary
            script_path = "./download_data.sh"
            subprocess.run(["bash", script_path], check=True)
        if arg == "--nucleus":
            fname  = str(sys.argv[sys.argv.index(arg)+1])

            for MT in MT_list[fname]:
                if recalculate_flag == True:
                    converter.convertENDF(fname)
                    converter.separateData(fname, MT)
                    processor.getEnergyAngleDistribtion(fname, MT, points, normcheck=True)
                if MT==4:
                    print("Trying to insert into NeuCBOT " + fname + " data for total (a,n)-reaction.", file=sys.stdout)
                else:    
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