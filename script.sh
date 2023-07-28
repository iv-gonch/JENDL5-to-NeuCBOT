#!/bin/bash

echo "Start!"

#====================Конвертировать файлы===============================

echo "converting..."

python3 ./main.py -convert Al27 &

python3 ./main.py -convert B10 &

python3 ./main.py -convert B11 &

python3 ./main.py -convert Be9 &

python3 ./main.py -convert C12 &

python3 ./main.py -convert C13 &

python3 ./main.py -convert F19 &

python3 ./main.py -convert Li6 &

python3 ./main.py -convert Li7 &

python3 ./main.py -convert N14 &

python3 ./main.py -convert N15 &

python3 ./main.py -convert Na23 &

python3 ./main.py -convert O16 &

python3 ./main.py -convert O17 &

python3 ./main.py -convert O18 &

python3 ./main.py -convert Si28 &

python3 ./main.py -convert Si29 &

python3 ./main.py -convert Si30 &

#================Обработать данные======================================

# echo "processing..."

# python3 ./main.py -process Al27 6 50 &

# python3 ./main.py -process B10 6 50 &

# python3 ./main.py -process B11 6 50 &

# python3 ./main.py -process Be9 6 50 &

# python3 ./main.py -process C12 6 50 &

# python3 ./main.py -process C13 6 50 &

# python3 ./main.py -process F19 6 50 &

# python3 ./main.py -process Li6 6 50 &

# python3 ./main.py -process Li7 6 50 &

# python3 ./main.py -process N14 6 50 &

# python3 ./main.py -process N15 6 50 &

# python3 ./main.py -process Na23 6 50 &

# python3 ./main.py -process O16 6 50 &

# python3 ./main.py -process O17 6 50 &

# python3 ./main.py -process O18 6 50 &

# python3 ./main.py -process Si28 6 50 &

# python3 ./main.py -process Si29 6 50 &

# python3 ./main.py -process Si30 6 50 &
                 
#================Построить графики======================================
# python3 ./main.py -graph fname MF MT points dimension

# echo "graphing..."

# python3 ./main.py -graph Al27 6 50 100 3 &

# python3 ./main.py -graph B10 6 50 100 3 &

# python3 ./main.py -graph B11 6 50 100 3 &

# python3 ./main.py -graph Be9 6 50 100 3 &

# python3 ./main.py -graph C12 6 50 100 3 &

# python3 ./main.py -graph C13 6 50 100 3 &

# python3 ./main.py -graph F19 6 50 100 3 &

# python3 ./main.py -graph Li6 6 50 100 3 &

# python3 ./main.py -graph Li7 6 50 100 3 &

# python3 ./main.py -graph N14 6 50 100 3 &

# python3 ./main.py -graph N15 6 50 100 3 &

# python3 ./main.py -graph Na23 6 50 100 3 &

# python3 ./main.py -graph O16 6 50 100 3 &

# python3 ./main.py -graph O17 6 50 100 3 &

# python3 ./main.py -graph O18 6 50 100 3 &

# python3 ./main.py -graph Si28 6 50 100 3 &

# python3 ./main.py -graph Si29 6 50 100 3 &

# python3 ./main.py -graph Si30 6 50 100 3 &

#=======================================================================

echo "Done!"