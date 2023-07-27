#!/usr/bin/python
# -*- coding: utf-8 -*-

# Считывает строки с конкретными MF и MT из конвертированного файла. 
# Записывает в папку /processed/filename/MF**_MT***/NK**_NE*** функцию p_i(theta) для каждой энергии налетающей альфа частицы

from __future__ import print_function
from __future__ import division
import numpy as np
import math
import sys
import os

import constants
import converter
import polynomials


def writeData(fname, MF, MT):

    if not os.path.isfile('converted/' + fname):    # проверка наличия конвертированного файла
        print('There is no converted', fname, 'file!', file=sys.stdout)
        converter.convertENDF(fname)
    f = open('converted/' + fname)

    f1 = open('converted/' + fname) # тут мы просто открываем любой файл. Потом, в цикле, 
    # будем открывать нужные файлы, когда узнаем их расположение. (Цикл начинается с закрытия файла, для этого нужна эта строка)

    if not os.path.isdir('processed'):  # проверка наличия директории
        os.mkdir('processed')
    
    if not os.path.isdir('processed/' + fname): # проверка наличия директории
        os.mkdir('processed/' + fname)

    if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)): # проверка наличия директории
        os.mkdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT))

    NWlineNumber = [0]  # номер подтаблицы (каждая соответствует своей энергии налетающей частицы E_in)
    tmp = 0     # тк в ENDF таблицы размазанны в строки по 6 элементов, иногда несколько ячеек в строке остаются пустыми.
                # Эта переменная позволяет не записывать пустые ячейки в память 
    counter = 0 # счётчик номера NW (всего их NE штук)
    NP = 0      # нужен чтобы правильно определять номер строки с NE 
    
    for line in f.readlines():  # считываем построчно
        
        word = converter.convertLine(line)  # разбиваем строку на массив numpy, состоящий из 10 элементов

        if (int(word[constants.ENDF.MFindex]) == MF and int(word[constants.ENDF.MTindex]) == MT): # читаем только нужные строчки по MF, MT
            # ниже просто запоминаем шапку таблицы, может потом пригодится. Вид первых трёх строк всегда одинаков (в MF6 как минимум)
            # подробнее про смысл констант см. файл constants.py (краткая справка) или ENDF6 formats manual 
            # https://www-nds.iaea.org/public/endf/endf-manual.pdf
            NS = int(word[constants.ENDF.NSindex])  # номер текущей строки
            if (NS == 1):    # ищем NK. Он всегда на 1й строке
                ZA = int(word[constants.ENDF.ZAindex])
                AWR = float(word[constants.ENDF.AWRindex])
                JP = int(word[constants.ENDF.JPindex])
                if (JP != 0): print('JP != 0 for', fname)   # проверка на всякий случай
                LCT = int(word[constants.ENDF.LCTindex])    
                if (LCT != 2): print(fname, 'data is given not in laboratory system') # проверка системы отсчёта
                NK = int(word[constants.ENDF.NKindex])
                if (NK > 1): print(fname, 'MF', MF, 'MT', MT, 'contains data of more than one product particle') # проверка количества вылетающих частиц
            if (NS == 2):    # ищем NP. Он всегда на 2й строчке
                ZAP = int(word[constants.ENDF.ZAPindex])
                AWP = float(word[constants.ENDF.AWPindex])
                if (int(AWP) != 1 or int(ZAP) != 1): print('Product particle is not neutron for', fname)    # проверка на вылетающую частицу
                LIP = int(word[constants.ENDF.LIPindex])
                if (LIP != 0): print('LIP != 0 for', fname) # проверка на всякий случай
                LAW = int(word[constants.ENDF.LAWindex])
                if (LAW != 2): print('LAW != 2 for', fname) # если LAW!=2, то надо читать мануал и дописывать новый функционал
                # NR = int(word[constants.ENDF.NRindex])      # встречается ещё один NR. Но оба не используются
                NP = int(word[constants.ENDF.NPindex])      # нужен чтобы правильно определять номер строки с NE 
            
            if (NS == 3): 
                NBT = int(word[constants.ENDF.NBTindex])    # не уверен что это NBT
                INT = int(word[constants.ENDF.INTindex])    # не уверен что это INT
            
            # if (NS <= 3): # вывод шапки таблицы в консоль

            if (NS == 4 + math.ceil(NP/3)):   # если номер строки таков, то в ней лежит NE (и NR)
                NE = int(word[constants.ENDF.NEindex])  # записываем чему равно NE
                NWlineNumber[0] = int(word[constants.ENDF.NSindex] + 2) # записываем в какой строке ожидать следующее значение NW

            if (NS == int(NWlineNumber[counter])): # номер строоки с очередным NW, LANG, E_in (и NL)
                NWlineNumber.append(NWlineNumber[counter] + math.ceil(int(word[constants.ENDF.NWindex])/6) + 1)
                # записываем в какой строке ожидать следующее значение NW
                counter += 1    # счётчик номера E_in 
                f1.close()  # закрываем файл с предыдущим E_in

                if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)):  # проверка наличия директории
                    os.mkdir ('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT))
                f1 = open('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter), 'w')
                # создаём и открываем файл на пути /processed/C13/MF6_MT50/NK1_NE47 (например)
                f1.write('MF = ' + str(MF) + '\tMT = ' + str(MT) +'\nEmitted particle ZAP code = ' + str(ZAP) + '\nAmount of files in directory for this type of particle: ' + str(NE) + '\n')
                # записываем MF, MT и число табличек с разными энергиями влетающих частиц E_in
                f1.write('\nIncident particle energy (eV) = \n' + str(word[constants.ENDF.IncidentEnergyindex]) + '\n\nAmount of points in this file: ' + str(int(word[constants.ENDF.NWindex])) + '\n')
                # записываем E_in и число точек

                if (int(word[constants.ENDF.LANGindex]) != 0):  # если LANG!=0, то надо читать мануал и дописывать код
                    print('LANG != 0 for', fname, 'line', NS)

                tmp = int(word[constants.ENDF.NWindex]) # счётчик количества точек для конкретного E_in

            if (counter > 0 and NS > NWlineNumber[counter-1]):
                for i in range(6):
                    if(i < tmp):    # чтобы не выводить нули из строки, которые являются не значениями, а символами пустых ячеек                      
                        f1.write(str(word[i]) + '\n')   # записываем в файл экспериментальное значение без изменений
                tmp -= 6    # строка прошла, значит количество оставшихся значений уменьшилось на 6            
    f.close()


# def giveData(fname, MF, MT):    # попытка считать данные без создания кучи записей 
# # (провалилась из-за того, что длина подтабличек может быть разной (для каждой E_in своё NW))
# # массивы numpy не динамические, поэтому без двойного считывания файла не обойтись.
# # использовать динамические массивы питона не пробовал, но это родит ряд новых проблем

#     if not os.path.isfile('converted/' + fname):    # проверка наличия конвертированного файла
#         print('There is no converted', fname, 'file!', file=sys.stdout)
#         converter.convertENDF(fname)
#     f = open('converted/' + fname)

#     NWlineNumber = [0]  # номер подтаблицы (каждая соответствует своей энергии налетающей частицы E_in)
#     tmp = 0     # тк в ENDF таблицы размазанны в строки по 6 элементов, иногда несколько ячеек в строке остаются пустыми.
#                 # Эта переменная позволяет не записывать пустые ячейки в память 
#     counter = 0 # счётчик номера NW (всего их NE штук)
#     NP = 0      # нужен чтобы правильно определять номер строки с NE 
    
#     for line in f.readlines():  # считываем построчно
        
#         word = converter.convertLine(line)

#         if (int(word[constants.ENDF.MFindex]) == MF and int(word[constants.ENDF.MTindex]) == MT): # читаем только нужные строчки по MF, MT
#             # ниже просто запоминаем шапку таблицы, может потом пригодится. Вид первых трёх строк всегда одинаков (в MF6 как минимум)
#             # подробнее про смысл констант см. файл constants.py (краткая справка) или ENDF6 formats manual 
#             # https://www-nds.iaea.org/public/endf/endf-manual.pdf
#             NS = int(word[constants.ENDF.NSindex])  # номер текущей строки
#             if (NS == 1):    # ищем NK. Он всегда на 1й строке
#                 ZA = int(word[constants.ENDF.ZAindex])
#                 AWR = float(word[constants.ENDF.AWRindex])
#                 JP = int(word[constants.ENDF.JPindex])
#                 if (JP != 0): print('JP != 0 for', fname)   # проверка на всякий случай
#                 LCT = int(word[constants.ENDF.LCTindex])    
#                 if (LCT != 2): print('Data given in', fname, 'is not in laboratory system') # проверка системы отсчёта
#                 NK = int(word[constants.ENDF.NKindex])
            
#             if (NS == 2):    # ищем NP. Он всегда на 2й строчке
#                 ZAP = int(word[constants.ENDF.ZAPindex])
#                 AWP = float(word[constants.ENDF.AWPindex])
#                 if (int(AWP) != 1 or int(ZAP) != 1): print('Product particle is not neutron for', fname)    # проверка на вылетающую частицу
#                 LIP = int(word[constants.ENDF.LIPindex])
#                 if (LIP != 0): print('LIP != 0 for', fname) # проверка на всякий случай
#                 LAW = int(word[constants.ENDF.LAWindex])
#                 if (LAW != 2): print('LAW != 2 for', fname) # если LAW!=2, то надо читать мануал и дописывать новый функционал
#                 # NR = int(word[constants.ENDF.NRindex])      # встречается ещё один NR. Но оба не используются
#                 NP = int(word[constants.ENDF.NPindex])      # нужен чтобы правильно определять номер строки с NE 
            
#             if (NS == 3): 
#                 NBT = int(word[constants.ENDF.NBTindex])    # не уверен что это NBT
#                 INT = int(word[constants.ENDF.INTindex])    # не уверен что это INT
            
#             # if (NS <= 3): # вывод шапки таблицы в консоль

#             if (NS == 4 + math.ceil(NP/3)):   # если номер строки таков, то в ней лежит NE (и NR)
#                 NE = int(word[constants.ENDF.NEindex])  # записываем чему равно NE
#                 NWlineNumber[0] = int(word[constants.ENDF.NSindex] + 2) # записываем в какой строке ожидать следующее значение NW

#             if (NS == int(NWlineNumber[counter])): # номер строоки с очередным NW, LANG, E_in (и NL)
#                 NWlineNumber.append(NWlineNumber[counter] + math.ceil(int(word[constants.ENDF.NWindex])/6) + 1)
#                 # записываем в какой строке ожидать следующее значение NW
#                 counter += 1    # счётчик номера E_in 
#                 if (counter == 1):
#                     A = np.zeros((int(word[constants.ENDF.NWindex]), NE), dtype = float)
#                 if (int(word[constants.ENDF.LANGindex]) != 0):  # если LANG!=0, то надо читать мануал и дописывать код
#                     print('LANG != 0 for', fname, 'line', NS)
#                 tmp = int(word[constants.ENDF.NWindex]) # счётчик количества точек для конкретного E_in

#             if (counter != 0 and NS != NWlineNumber[counter-1]):
#                 # не заходим в цикл если ещё не считали ни одного NW (counter=!=0)
#                 # и если мы ещё не прошли строку, в которой нынешний MW считывается (NS != NWlineNumber[counter-1])
#                 for i in range(6):
#                     if(i < tmp):    # чтобы не выводить нули из строки, которые являются не значениями, а символами пустых ячеек                      
#                         A[(NS - NWlineNumber[counter-1]-1)*6 + i][counter-1] = word[i]
#                 tmp -= 6    # строка прошла, значит количество оставшихся значений уменьшилось на 6     

#     f.close()
#     return A