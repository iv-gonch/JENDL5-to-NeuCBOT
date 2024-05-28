#!/usr/bin/python
# -*- coding: utf-8 -*-

# Файл преобразует стандартную запись JENDL (один файл - один изотоп и одна налетающая частица) в читаемый для питона вид

from __future__ import print_function
from __future__ import division
import numpy as np
import math
import sys
import os

import constants
import chemistry
# import chemistry
# import polynomials


def convertLine(line):  # чтение в конвертированном файле

    word = np.zeros(10, dtype = float)  # каждый элемент строки файла будем записывать в виде float в массив numpy. Изначально всё - вещественны нули
    if (line[83:85] != " 0" and line[83:85] != " 1"):   # отсекаем строки с текстом (те. с MF=" 1" или =" 0", MT=" 451")
        for i in range(10): # цикл нужен чтобы под float() попали только элементы строки, состоящие из цифр (иначе ошибка)
            if (line.strip("|").split("|")[i].strip() != ""):   # пустые слова остаются вещественными нулями в word[]
                word[i] = float(line.strip("|").split("|")[i].strip())  # в конвертированных файлах разделителем является "|" 
    return word


def convertENDF(fname): # convert Evaluated Nuclear Data File

    word = ["0"] * 10   # слова из необработанного файла
    new_word = word     # обработанные слова, записываемые в новый файл

    # if not os.path.isfile("downloaded/" + fname):   # проверка наличия скачанного файла
    #     print("There is no downloaded", fname, "file!", file=sys.stdout)
    Z = chemistry.getZ(fname.split("_")[0])
    Ele = fname.split("_")[0]
    A = int(fname.split("_")[1])
    JENDL_fname = "a_" + str("{:03}".format(Z)) + "-" + Ele.capitalize() + "-" + str("{:03}".format(A)) + ".dat"

    if not os.path.isfile("jendl5-a/" + JENDL_fname):   # проверка наличия скачанного файла
        print("There is no downloaded", fname, "file!", file=sys.stdout)
        # loader.JENDL5(fname)  # круто бы дописать
    else:
        f = open("jendl5-a/" + JENDL_fname) # считываем первую строку чтобы стандартизированно назвать конвертированный файл
        line1 = f.readline()[12:18] # на этом месте в файлах JENDL-5 записано название элемента и его массовое число
        ele = line1[:2].strip()     # название элемента
        A = int(line1[4:])  # массовое число
        f.close()   # не уверен что после readline() правильно сработает метод readlines(). поэтому открываю и закрываю. Если первая строка не пропустится, то можно забить

        f = open("jendl5-a/" + JENDL_fname)     
        print("New file", fname, "will be saved as ./converted/", ele + "_" + str(A), file=sys.stdout)
        
        if not os.path.isdir("converted"):
            os.mkdir("converted")
        f1= open("converted/" + ele + "_" + str(A), "w")

        for line in f.readlines():  # читаем файл построчно

            for i in range(len(constants.ENDF.lineMarkup)-1): # разбиваем его на "слова" в соответсвии с правилами ENDF (первые 6 слов - 11 символов и тд.)
                word[i] = line[constants.ENDF.lineMarkup[i]:constants.ENDF.lineMarkup[i+1]]

                if (i>=6):   # если имеем дело с элементами с 7го по 10й, то там гарантировано стоят натуральные числа
                    new_word[i] = word[i] + "|" # добавляем "|" между числами, чтобы читать их методом .split
                else:   # если имеем дело с элементами с 1го по 6й, то там могут быть буквы, натуральные и вещественные числа, пропуски
                    if ((line[70:72] != " 0" and line[70:72] != " 1") or (int(line[75:]) > 0 and int(line[75:]) < 5)):   # отсекаем строки с текстом (те. с MF=" 1" или =" 0", MT=" 451")
                        if (word[i][2] == "."): # переводим экспоненциальную запись вида +0.0+0 в +0.0е+0
                            # если вдруг бывает, что точка в числе есть, но не на 3м месте, то надо переписать через .find()
                            if (word[i][1:].find("+") != -1):
                                new_word[i] = word[i][0] + word[i][1:].split("+")[0] + "e+" + word[i][1:].split("+")[1]  
                            elif (word[i][1:].find("-") != -1):
                                new_word[i] = word[i][0] + word[i][1:].split("-")[0] + "e-" + word[i][1:].split("-")[1]
                        else: # тут будут либо целые числа, либо пробелы
                            new_word[i] = " " + word[i] # добавляем " " чтобы уравнять длину с вещественными числами (там добавилась "e")
                        new_word[i] = new_word[i] + "|" # добавляем "|" между числами, чтобы читать их методом .split
                    else:                       # читаем строки с текстом 
                        new_word[i] = word[i]   # их оставляем без изменений
                        new_word[5] = new_word[5] + " "*11 + "|"  # сдвигаем элементы 7-10, чтобы везде в файле у них было одно положение
                            # добавляем "|" в конце текста, чтобы читать эти строки методом .split (в тексте чтение будет отличаться от таблиц)

                f1.write(new_word[i])   # наконец записываем в файл
            f1.write("\n")  # новая строка
        f.close()
        f1.close()


def separateData(fname, MT):   # считывает из ./converted, записывает в ./reshaped по отдельным папкам

    if not os.path.isdir("reshaped"):  # проверка наличия директории
        os.mkdir("reshaped")
    
    # ==================  запись коэффициентов Лежандра  ================== #
    MF = int(6) 
    if not os.path.isfile("converted/" + fname):    # проверка наличия конвертированного файла
        print("There is no converted", fname, "file!", file=sys.stdout)
        convertENDF(fname)

    f = open("converted/" + fname)
    f1 = open("converted/" + fname) # тут мы просто открываем файл. Потом, в цикле, будем открывать нужные файлы, 
    # когда узнаем их расположение. (тк цикл начинается с закрытия файла, для этого нужно сперва открыть)

    NWlineNumber = [0]  # номер подтаблицы (каждая соответствует своей энергии налетающей частицы E_in)
    tmp = 0     # тк в ENDF таблицы размазанны в строки по 6 элементов, иногда несколько ячеек в строке остаются пустыми.
                # Эта переменная позволяет не записывать пустые ячейки в память 
    counter = 0 # счётчик номера NW (всего их NE штук)
    NP = 0      # нужен чтобы правильно определять номер строки с NE 

    for line in f.readlines():  # считываем построчно
        word = convertLine(line)  # разбиваем строку на массив numpy, состоящий из 10 элементов
        if (int(word[constants.ENDF.MFindex]) == 6 and int(word[constants.ENDF.MTindex]) == MT): # читаем только нужные строчки по MF, MT

            if not os.path.isdir("reshaped/" + fname): # проверка наличия директории
                os.mkdir("reshaped/" + fname)
            if not os.path.isdir("reshaped/" + fname + "/MF" + str(MF) + "_MT" + str(MT)): # проверка наличия директории
                os.mkdir("reshaped/" + fname + "/MF" + str(MF) + "_MT" + str(MT))

            # ниже просто запоминаем шапку таблицы, может потом пригодится. Вид первых трёх строк всегда одинаков (в MF6 как минимум)
            # подробнее про смысл констант см. файл constants.py (краткая справка) или ENDF6 formats manual 
            # https://www-nds.iaea.org/public/endf/endf-manual.pdf
            NS = int(word[constants.ENDF.NSindex])  # номер текущей строки

            if (NS == 1):    # ищем NK. Он всегда на 1й строке
                ZA = int(word[constants.ENDF.ZAindex])
                AWR = float(word[constants.ENDF.AWRindex])
                JP = int(word[constants.ENDF.JPindex])
                if (JP != 0): print("JP != 0 for", fname)   # проверка на всякий случай
                LCT = int(word[constants.ENDF.LCTindex])    
                if (LCT != 2): print(fname, "data is given not in laboratory system") # проверка системы отсчёта
                NK = int(word[constants.ENDF.NKindex])
                if (NK > 1): print(fname, "MF", MF, "MT", MT, "contains data of more than one product particle") # проверка количества вылетающих частиц
            
            if (NS == 2):    # ищем NP. Он всегда на 2й строчке
                ZAP = int(word[constants.ENDF.ZAPindex])
                AWP = float(word[constants.ENDF.AWPindex])
                if (int(AWP) != 1 or int(ZAP) != 1): print("Product particle is not neutron for", fname)    # проверка на вылетающую частицу
                LIP = int(word[constants.ENDF.LIPindex])
                if (LIP != 0): print("LIP != 0 for", fname) # проверка на всякий случай
                LAW = int(word[constants.ENDF.LAWindex])
                if (LAW != 2): print("LAW != 2 for", fname) # если LAW!=2, то надо читать мануал и дописывать новый функционал
                NR = int(word[constants.ENDF.NRindex])      # встречается ещё один NR. Но оба не используются
                if (NR != 1): print("NR != 1 in line 2 for", fname, "MF", MF, "MT", MT)
                NP = int(word[constants.ENDF.NPindex])      # нужен чтобы правильно определять номер строки с NE 

            if (NS == 3): 
                NBT = int(word[constants.ENDF.NBTindex])    # не уверен что это NBT
                INT = int(word[constants.ENDF.INTindex])    # не уверен что это INT
            
            # if (NS <= 3): # вывод шапки таблицы в консоль
            if (NS == 4 + math.ceil(NP/3)):   # если номер строки таков, то в ней лежит NE (и NR)
                NR = int(word[constants.ENDF.NRindex])      # # встречается ещё один NR. Но оба не используются
                if (NR != 1): print("NR != 1 in line", str(NS), "for", fname, "MF", MF, "MT", MT)
                NE = int(word[constants.ENDF.NEindex])  # записываем чему равно NE
                NWlineNumber[0] = int(word[constants.ENDF.NSindex] + 2) # записываем в какой строке ожидать следующее значение NW
            
            if (NS == int(NWlineNumber[counter])): # номер строоки с очередным NW, LANG, E_in (и NL)
                NWlineNumber.append(NWlineNumber[counter] + math.ceil(int(word[constants.ENDF.NWindex])/6) + 1)
                # записываем в какой строке ожидать следующее значение NW
                f1.close()  # закрываем файл с предыдущим E_in

                f1 = open("reshaped/" + fname + "/MF" + str(MF) + "_MT" + str(MT) + "/NK" + str(NK) + "_NE" + str(counter), "w")
                # создаём и открываем файл на пути /reshaped/C13/MF6_MT50/NK1_NE47 (например)

                f1.write("ZA = " + str(ZA) + "\tAWR = " + str(AWR) + "\nMF = " + str(MF) + "\tMT = " + str(MT) + \
                        "\nZAP (Emitted particle ZA code) = " + str(ZAP) + "\nAmount of files in directory for this type of particle: " + str(NE) + "\n")
                # записываем MF, MT и число табличек с разными энергиями влетающих частиц E_in
                f1.write("\nIncident particle energy (eV) = \n" + str(word[constants.ENDF.IncidentEnergyindex]) + \
                        "\n\nAmount of points in this file: " + str(int(word[constants.ENDF.NWindex])) + "\n")
                # записываем E_in и число точек

                if (int(word[constants.ENDF.LANGindex]) != 0):  # если LANG!=0, то надо читать мануал и дописывать код
                    print("LANG != 0 for", fname, "line", NS)
                tmp = int(word[constants.ENDF.NWindex]) # счётчик количества точек для конкретного E_in
                counter += 1    # счётчик номера E_in 
            if (counter > 0 and NS > NWlineNumber[counter-1]):
                for i in range(6):
                    if(i < tmp):    # чтобы не выводить нули из строки, которые являются не значениями, а символами пустых ячеек                      
                        f1.write(str(word[i]) + "\n")   # записываем в файл экспериментальное значение без изменений
                tmp -= 6    # строка прошла, значит количество оставшихся значений уменьшилось на 6            
    f.close()
    f1.close()

    # ==================  запись парциальных сечений реакций (a, nx)  ================== # 
    MF = int(3)
    dirname = fname + "/MF" + str(MF) + "_MT" + str(MT)       # C_13/MF3_MT50
    
    if not os.path.isdir("reshaped/" + fname): # проверка наличия директории
        os.mkdir("reshaped/" + fname)
    file1 = open("./converted/" + fname, "r")   # файл из папки converted из ENDF6-reader 
    file2 = open("./reshaped/" + dirname, "w")  # файл в который ведётся запись 
    while True:
        line = file1.readline()
        # прерываем цикл, если строка пустая 
        if not line:
            break
        if ((line[83:85] != " 1") and (line[83:85] != " 0")):
            if ((int(line.split("|")[7]) == MF) and \
                (int(line.split("|")[8]) == MT) and \
                (int(line.split("|")[9]) >= 4)):
                file2.write(line.split("|")[0] + " " + \
                            line.split("|")[1] + "\n")
                file2.write(line.split("|")[2] + " " + \
                            line.split("|")[3] + "\n")
                file2.write(line.split("|")[4] + " " + \
                            line.split("|")[5] + "\n")
    file2.close()
    file1.close()