#!/usr/bin/python
# -*- coding: utf-8 -*-

# Считывает данные конкретного MF и MT из конвертированного файла. 
# Записывает в папку /processed/ функцию p_i(theta) для каждой энергии налетающей альфа частицы

from __future__ import print_function
from __future__ import division
import numpy as np
import math
import sys
import os

import constants
import converter
import polynomials

def processData(fname, MF, MT):

    if not os.path.isfile('converted/' + fname):    # проверка наличия конвертированного файла
        print('There is no converted', fname, 'file!', file=sys.stdout)
        converter.convertENDF(fname)
    f = open('converted/' + fname)
    f1 = open('converted/' + fname)
    if not os.path.isdir('processed'):
        os.mkdir('processed')
    
    if not os.path.isdir('processed/' + fname):
        os.mkdir('processed/' + fname)

    if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)):
        os.mkdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT))

    # if not os.path.isdir('processed/' + fname + '/MF' + MF + 'MT' + MT + '/NK' + NK + '_NE' + NE + '/'):
    #     os.mkdir("processed" + fname + '/MF' + MF + 'MT' + MT + '/NK' + NK + '_NE' + NE)

    # f1 = open('processed/' + fname + '_MF' + str(MF) + '_MT' + str(MT), 'w')
    
    # ftest = open('test/' + fname + '_MF' + str(MF) + '_MT' + str(MT), 'w')

    NElineNumber = -1
    NWlineNumber = [0]
    tmp = 0
    counter = 0 # счётчик номера NW (всего их NE штук)
    NP = 0
    
    for line in f.readlines():

        word = np.zeros(10, dtype = float)
        
        if (line[83:85] != ' 0' and line[83:85] != ' 1'):   # отсекаем строки с текстом (те. с MF=' 1' или =' 0', MT=' 451')
            for i in range(10): # такие сложности нужны чтобы под float() попали только слова из цифр (иначе ошибка)
                if (line.strip('|').split('|')[i].strip() != ''):   # пустые слова становятся нецелыми нулями, и сохраняются в word[]
                    word[i] = float(line.strip('|').split('|')[i].strip())  # в конвертированных файлах разделителем является '|' 
            
            # ftest.write(str(int(word[constants.ENDF.MFindex])) + '|' + str(int(word[constants.ENDF.MTindex])) + '\n')

            # ftest.write(str(int(word[8]))+'\n')
            # if (int(word[8]) == MT and int(word[7]) == MF):
            #     print (MF, MT)
            #     print('------')
            #     print (int(word[constants.ENDF.MFindex]), int(word[constants.ENDF.MTindex]))

        if (int(word[constants.ENDF.MFindex]) == MF and int(word[constants.ENDF.MTindex]) == MT): # читаем только нужные строчки

            if (int(word[constants.ENDF.NSindex]) == 1): 
                # print('a')
                ZA = int(word[constants.ENDF.ZAindex])
                AWR = float(word[constants.ENDF.AWRindex])
                JP = int(word[constants.ENDF.JPindex])
                LCT = int(word[constants.ENDF.LCTindex])
                NK = int(word[constants.ENDF.NKindex])
            
            if (int(word[constants.ENDF.NSindex]) == 2):    # ищем NP. Он всегда на 2й строчке
                # print('b')
                ZAP = int(word[constants.ENDF.ZAPindex])
                AWP = float(word[constants.ENDF.AWPindex])
                LIP = int(word[constants.ENDF.LIPindex])
                LAW = int(word[constants.ENDF.LAWindex])
                if (LAW != 2): print('LAW != 2 for', fname)
                # NR = int(word[constants.ENDF.NRindex])    # встречается ещё один NR. Но оба не используются
                NP = int(word[constants.ENDF.NPindex])
            
            if (int(word[constants.ENDF.NSindex]) == 3): 
                # print('c')
                NBT = int(word[constants.ENDF.NBTindex])  # не уверен что это NBT
                INT = int(word[constants.ENDF.INTindex])  # не уверен что это INT
            
            # if (int(word[constants.ENDF.NSindex]) <= 3): # вывод шапки таблицы в консоль
            #     print(word)   

            if (int(word[constants.ENDF.NSindex]) == 4 + math.ceil(NP/3)):   # номер строки с NE
                # или использовать math.floor
                # print('NE fere!')
                NE = int(word[constants.ENDF.NEindex])
                NElineNumber = int(word[constants.ENDF.NSindex])
                # counter = 0   счётчик номера NW (всего их NE штук)
                # NWlineNumber = np.zeros(NE, dtype = int)  # не заработало тк надо инициализировать вне ифа (код не интерпретируется)
                NWlineNumber[0] = int(NElineNumber + 2)  # номера строк содержащих NW
                # print(NWlineNumber)
                # NWlineNumber[counter] = NElineNumber + 1    # номера строк содержащих NW

            if (int(word[constants.ENDF.NSindex]) == int(NWlineNumber[counter])): # номер строоки с очередным NW
                # print('NW here!')
                counter += 1
                NWlineNumber.append(NWlineNumber[counter-1] + math.ceil(int(word[constants.ENDF.NWindex])/6) + 1)
                
                f1.close()

                if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)):
                    os.mkdir ('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT))
                f1 =     open('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter), 'w')

                f1.write('MF = ' + str(MF) + '\tMT = ' + str(MT) + '\nAmount of files in directory: ' + str(NE) + '\n')
                # print('NE found:', NE)

                f1.write('\nIncident particle energy (eV) = \n' + str(word[constants.ENDF.IncidentEnergyindex]) + '\n\nAmount of points: ' + str(int(word[constants.ENDF.NWindex])) + '\n')
                # записываем E_in и число точек

                if (int(word[constants.ENDF.LANGindex]) != 0): print('LANG != 0 for', fname, 'line', int(word[constants.ENDF.NSindex]))
                tmp = int(word[constants.ENDF.NWindex]) # счётчик количества точек для конкретного E_in
                # print ('NW', counter, 'found:', NWlineNumber[counter])

            if (counter > 0 and int(word[constants.ENDF.NSindex]) > NWlineNumber[counter-1]):
                for i in range(6):
                    if(i < tmp):    # чтобы не выводить нули из строки, которые являются не значениями, а символами пустых ячеек
                    # if (int(word[i]) != -1):   # проверка наличия числа в ячейке строки
                        
                        f1.write(str(word[i]) + '\n')   # записываем в файл экспериментальное значение без изменений
                tmp -= 6    # строка прошла, значит количество оставшихся значений уменьшилось на 6
            # print('weewoo')

            

            # if (word[:4] == [0.]*4):    # строка с заданием NR, NE по правилам начинается с 4х нулей. Использую как маркер. Мб ещё где-то такое встречается
            #     # NR = word[constants.ENDF.NRindex]   # встречается ещё один NR. Но оба не используются
            #     NE = word[constants.ENDF.NEindex]
            #     NSstart = int(word[constants.ENDF.NSindex])  
            #     print(NR, NE, NSstart)
            
            
    f.close()
    # f1.close()