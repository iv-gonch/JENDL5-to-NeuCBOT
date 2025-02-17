#!/usr/bin/python
# -*- coding: utf-8 -*-

# финальный этап работы ENDF6reader. 
# Интерполирует данные из stage_1_data/En_distribution 
# и записывает их в ../neucbot и в ./stage_2_data

from __future__ import print_function
from __future__ import division
import numpy as np
from scipy import interpolate
import os


MT_list =  {"Li_6" : [50, 51, 52, 53], 
            "Li_7" : [50, 51, 52, 53, 54], 
            "Be_9" : [50, 51, 52], 
            "B_10" : [50, 51, 52, 53, 54], 
            "B_11" : [50, 51, 52, 53, 54], 
            "C_12" : [50], 
            "C_13" : [50, 51, 52, 53, 54], 
            "N_14" : [50, 51, 52, 53, 54], 
            "N_15" : [50, 51, 52, 53, 54], 
            "O_17" : [50, 51, 52, 53], 
            "O_18" : [50, 51, 52, 53, 54], 
            "F_19" : [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], 
            "Na_23": [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]}


def summ_data(fname):

    for isotope in MT_list:
        if not os.path.isdir("./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4"):
            os.mkdir        ("./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4")

        # Исходный файл и целевой файл
        destination_file = "./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4/" + fname
        source_file =      "./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT50/" + fname
        # Копирование файла 
        with open(source_file, 'rb') as src, open(destination_file, 'wb') as dst:
            dst.write(src.read())


        for MT in MT_list[isotope]: 
            if MT > 50:
                f = open("./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT" + str(MT) + "/cross-section", "r") 
                XS_src = []
                E_a = []

                F = open("./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT4/cross-section", "r") 
                XS_dst = []

                for line in f.readlines():
                    if line[0] == "#":
                        continue
                    XS_src.append(float(line.split()[1]))
                    E_a.append(float(line.split()[0]))

                for line in F.readlines():
                    if line[0] == "#":
                        continue
                    XS_dst.append(float(line.split()[1]))
                f.close()
                F.close()

                XS_src = np.array(XS_src)
                E_a = np.array(E_a)
                XS_dst = np.array(XS_dst)

                XS_res = XS_src + XS_dst

                F = open("./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT4/" + fname, "w") 
                F.write("# E_a, MeV\t\tXS, mb\n")

                for i in range(len(XS_res)):
                    F.write(str(E_a[i])  + " \t\t" + str(XS_res[i]) + "\n")
                F.close()


def main():
    summ_data("cross-section")

    dirname = "./stage_2_data/C/C13/JendlOut/MT50"
    dirLen = len([name for name in os.listdir(dirname)])    # число файлов в папке
    for i in range(dirLen - 1):
        fname = "outputE" + str("{:.4f}".format(i/100))
        summ_data(fname)

if __name__ == "__main__":
    main()