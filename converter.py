#!/usr/bin/python
# -*- coding: utf-8 -*-

# Файл преобразует стандартную запись JENDL (один файл - один изотоп и одна налетающая частица) в читаемый для питона вид

from __future__ import print_function
from __future__ import division
import sys
import os

import constants

def convertENDF(fname):

    word = ['0'] * 10   # слова из необработанного файла
    new_word = word     # обработанные слова, записываемые в новый файл

    if not os.path.isfile('downloaded/' + fname):   # проверка наличия скачанного файла
        print('There is no downloaded', fname, 'file!', file=sys.stdout)
        # loader.JENDL5(fname)

    f = open('downloaded/' + fname)
    print('New file',fname, 'will be saved to ./converted/', file=sys.stdout)

    if not os.path.isdir('converted'):
        os.mkdir("converted")
    f1= open('converted/' + fname, 'w')
    for line in f.readlines():  # читаем файл построчно

        for i in range(len(constants.ENDF.lineMarkup)-1): # разбиваем его на "слова" в соответсвии с правилами ENDF (первые 6 слов - 11 символов и тд.)
            word[i] = line[constants.ENDF.lineMarkup[i]:constants.ENDF.lineMarkup[i+1]]

            if (i>=6):   # если имеем дело с элементами с 7го по 10й, то там гарантировано стоят натуральные числа
                new_word[i] = word[i] + '|' # добавляем '|' между числами, чтобы читать их методом .split
            else:   # если имеем дело с элементами с 1го по 6й, то там могут быть буквы, натуральные и вещественные числа, пропуски
                if (line[70:72] != ' 0' and line[70:72] != ' 1'):   # отсекаем строки с текстом (те. с MF=' 1' или =' 0', MT=' 451')
                    if (word[i][2] == '.'): # переводим экспоненциальную запись вида +0.0+0 в +0.0е+0
                        # если вдруг бывает, что точка в числе есть, но не на 3м месте, то надо переписать через .find()
                        if (word[i][1:].find('+') != -1):
                            new_word[i] = word[i][0] + word[i][1:].split('+')[0] + 'e+' + word[i][1:].split('+')[1]  
                        elif (word[i][1:].find('-') != -1):
                            new_word[i] = word[i][0] + word[i][1:].split('-')[0] + 'e-' + word[i][1:].split('-')[1]
                    else: # тут будут либо целые числа, либо пробелы
                        new_word[i] = ' ' + word[i] # добавляем ' ' чтобы уравнять длину с вещественными числами (там добавилась 'e')
                    new_word[i] = new_word[i] + '|' # добавляем '|' между числами, чтобы читать их методом .split
                else:                       # читаем строки с текстом 
                    new_word[i] = word[i]   # их оставляем без изменений
                    new_word[5] = new_word[5] + ' '*11 + '|'  # сдвигаем элементы 7-10, чтобы везде в файле у них было одно положение
                        # добавляем '|' в конце текста, чтобы читать эти строки методом .split (в тексте чтение будет отличаться от таблиц)

            f1.write(new_word[i])   # наконец записываем в файл
        f1.write('\n')  # новая строка
    f.close()
    f1.close()

