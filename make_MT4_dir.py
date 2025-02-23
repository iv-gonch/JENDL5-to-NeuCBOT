#!/usr/bin/python
# -*- coding: utf-8 -*-

# финальный этап работы ENDF6reader. 
# Интерполирует данные из stage_1_data/En_distribution 
# и записывает их в ../neucbot и в ./stage_2_data

from __future__ import print_function
from __future__ import division
import numpy as np # type: ignore
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


def readfileXS(fname):
    
    i = 0
    #!!!# Если поставить dE_a другим, то сломается #!!!#
    column_1 = np.arange(0.0, 15.01, 0.01)
    column_2 = np.zeros(1501)
    
    f = open(fname, 'r')
    for line in f.readlines():
        if line.startswith("#") or line == "":
            continue
        column_1[i] = line.split()[0]
        column_2[i] = line.split()[1]
        i += 1
    f.close()
    return column_1, column_2


def readfileOutputE(fname):
    
    i = 0
    #!!!# Если поставить dE_n другим, то сломается #!!!#
    column_1 = np.arange(0.1, 15.1, 0.1)
    column_2 = np.zeros(150)
    
    f = open(fname, 'r')
    for line in f.readlines():
        if line == "EMPTY": # Только для файлов "outputE..."
            break
        else:
            if line.startswith("#") or line == "":
                continue
            column_1[i] = line.split()[0]
            column_2[i] = line.split()[1]
            i += 1
    f.close()
    return column_1, column_2


def summ_dataXS(fname):

    for isotope in MT_list:
        if not os.path.isdir("./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4"):
            os.mkdir        ("./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4")

        # Исходный файл (MT50) и целевой файл (MT40)
        destination_file = "./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4/" + fname
        source_file =      "./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT50/" + fname
        # Копирование файла 
        source_column_1, source_column_2 = readfileXS(source_file)
        f = open(destination_file, 'w')
        for i in range(len(source_column_1)):
            f.write(str(source_column_1[i]) + "\t\t" + str(source_column_2[i]) + "\n")
        # Можно добавить шапку файлу позже
        f.close()
        
        for MT in MT_list[isotope]: 
            if MT > 50:
                fname_src = "./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT" + str(MT) + "/" + fname
                E_a, XS_src = readfileXS(fname_src)

                fname_dst = "./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT4/" + fname
                E_a, XS_dst = readfileXS(fname_dst)

                XS_res = XS_src + XS_dst

                F = open("./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT4/" + fname, "w") 

                for i in range(len(XS_res)):
                    F.write(str(E_a[i])  + " \t\t" + str(XS_res[i]) + "\n")
                F.close()


def summ_dataOutputE(fname):

    for isotope in MT_list:
        if not os.path.isdir("./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4"):
            os.mkdir        ("./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4")

        # Исходный файл (MT50) и целевой файл (MT40)
        destination_file = "./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT4/" + fname
        source_file =      "./stage_2_data/" + \
                            isotope.split("_")[0] + "/" + \
                            isotope.replace("_", "") + \
                            "/JendlOut/MT50/" + fname
        # Копирование файла 
        source_column_1, source_column_2 = readfileOutputE(source_file)
        f = open(destination_file, 'w')
        for i in range(len(source_column_1)):
            f.write(str(source_column_1[i]) + "\t\t" + str(source_column_2[i]) + "\n")
        # Можно добавить шапку файлу позже
        f.close()
        
        for MT in MT_list[isotope]: 
            if MT > 50:
                fname_src = "./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT" + str(MT) + "/" + fname
                E_a, XS_src = readfileOutputE(fname_src)

                fname_dst = "./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT4/" + fname
                E_a, XS_dst = readfileOutputE(fname_dst)

                XS_res = XS_src + XS_dst

                F = open("./stage_2_data/" + \
                        isotope.split("_")[0] + "/" + \
                        isotope.replace("_", "") + \
                        "/JendlOut/MT4/" + fname, "w") 

                for i in range(len(XS_res)):
                    F.write(str(E_a[i])  + " \t\t" + str(XS_res[i]) + "\n")
                F.close()


def main():
    summ_dataXS("cross-section")

    dirname = "./stage_2_data/C/C13/JendlOut/MT50"
    dirLen = len([name for name in os.listdir(dirname)])    # число файлов в папке
    for i in range(dirLen - 1):
        fname = "outputE" + str("{:.4f}".format(i/100))
        # !!! Файлы могут содержать только слово "EMPTY". Необходимо учесть !!!
        summ_dataOutputE(fname)

if __name__ == "__main__":
    main()