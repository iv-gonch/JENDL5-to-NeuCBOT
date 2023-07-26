#!/usr/bin/python
# -*- coding: utf-8 -*-

# Файл содержит номера строк ENDF, физические константы и флаги для выполнения кода

# подробнее про смысл констант см. ENDF6 formats manual 
# https://www-nds.iaea.org/public/endf/endf-manual.pdf

class ENDF:
    lineMarkup = [0,11,22,33,44,55,66,70,72,75,80]  # разметка строки ENDF. Числа соответствуют номеру первого символа каждого элемента
    ZAindex = ZAPindex = NBTindex = 0   # номер значения ZA (зарядовое число * 1000 + массовое число мишени), 
    # ZAP (то же самое для продукта реакции), NBT (?)
    AWRindex = AWPindex = INTindex = IncidentEnergyindex = 1 # номер значения AWR (масса мишени в массах нейтрона), 
    # AWP (то же самое для продукта реакциии), INT (?), IncidentEnergy (энергия влетающей частицы (в данном случае это альфа-частица))
    JPindex = LIPindex = LANGindex = 2  # номер значения JP (?), LIP (?), LANG (что-то про выбор метода интерполяции)
            # Про LANG при LAW=2 в мануале (стр.158)
            # LANG flag that indicates the representation:
                # LANG=0, Legendre expansion;
                # LANG=12, tabulation with pi(µ) linear in µ;   Где pi(µ)= количество простых чисел N : N <= µ
                # LANG=14, tabulation with log(pi) linear in µ.

            # Про LANG в общем описании в мануале (стр.153-157)
                # Legendre Coefficients Representation (LANG=1)
                # Kalbach-Mann Systematics Representation (LANG=2)
                # Tabulated Function Representation (LANG=11-15)
    LCTindex = LAWindex = 3 # номер значения LCT (код системы отсчёта), LAW (вид закона распреедления)
    NKindex = NRindex = NWindex = 4 # номер значения NK (число подсекций в секции  с данным MT),
    # NR (число областей интерполяций), NW (число записей для данной энергии (часто равно NL))

    NPindex = NEindex = NLindex = 5 # номер значения NP (?), 
    # NE (число экспериментов с разной энергий налетающей частицы), NL (число разных коэффициентов Лежандра)
    
    # названия переменных выше и описания к ним взяты для случая MF=6 LAW=2

    MATindex = 6  # место в строке, на котором стоит значение MAT (код элемента мишени)
    MFindex = 7   # место в строке, на котором стоит значение MF (код типа данных)
    MTindex = 8   # место в строке, на котором стоит значение MT (код типа реакции)
    NSindex = 9   # место в строке, на котором стоит значение MS (номер строки)
    
    # верно для всех файлов ENDF6

class physics:
    N_A = 6.0221409e+23
    MeV_to_keV = 1.e3
    mb_to_cm2 = 1.e-27
    year_to_s = 31536000
    min_bin = 0   # keV
    max_bin = 20000  # keV
    delta_bin = 100  # keV

class flags:
    run_talys = False
    run_alphas = True
    print_alphas = False
    download_data = False
    download_version = 2
    force_recalculation = False