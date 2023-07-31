#!/bin/bash

echo "Start!"

# # ====================Конвертировать файлы===============================

# echo "converting..."

# python3 ./main.py -convert Al_27 &

# python3 ./main.py -convert B_10 &

# python3 ./main.py -convert B_11 &

# python3 ./main.py -convert Be_9 &

# python3 ./main.py -convert C_12 &

# python3 ./main.py -convert C_13 &

# python3 ./main.py -convert F_19 &

# python3 ./main.py -convert Li_6 &

# python3 ./main.py -convert Li_7 &

# python3 ./main.py -convert N_14 &

# python3 ./main.py -convert N_15 &

# python3 ./main.py -convert Na_23 &

# python3 ./main.py -convert O_16 &

# python3 ./main.py -convert O_17 &

# python3 ./main.py -convert O_18 &

# python3 ./main.py -convert Si_28 &

# python3 ./main.py -convert Si_29 &

# python3 ./main.py -convert Si_30 &

# # ================Обработать данные======================================

# echo "reshaping..."

# python3 ./main.py -reshape Al_27 6 50 &

# python3 ./main.py -reshape B_10 6 50 &

# python3 ./main.py -reshape B_11 6 50 &

# python3 ./main.py -reshape Be_9 6 50 &

# python3 ./main.py -reshape C_12 6 50 &

# python3 ./main.py -reshape C_13 6 50 &

# python3 ./main.py -reshape F_19 6 50 &

# python3 ./main.py -reshape Li_6 6 50 &

# python3 ./main.py -reshape Li_7 6 50 &

# python3 ./main.py -reshape N_14 6 50 &

# python3 ./main.py -reshape N_15 6 50 &

# python3 ./main.py -reshape Na_23 6 50 &

# python3 ./main.py -reshape O_16 6 50 &

# python3 ./main.py -reshape O_17 6 50 &

# python3 ./main.py -reshape O_18 6 50 &

# python3 ./main.py -reshape Si_28 6 50 &

# python3 ./main.py -reshape Si_29 6 50 &

# python3 ./main.py -reshape Si_30 6 50 &
                 
# # ================Построить графики======================================
# # пример: python3 ./main.py -graph fname MF_ MT points dimension

echo "graphing..."

python3 ./main.py -graph Al_27 6 50 10 3D &

python3 ./main.py -graph B_10 6 50 10 3D &

python3 ./main.py -graph B_11 6 50 10 3D &

python3 ./main.py -graph Be_9 6 50 10 3D &

python3 ./main.py -graph C_12 6 50 10 3D &

python3 ./main.py -graph C_13 6 50 10 3D &

python3 ./main.py -graph F_19 6 50 10 3D &

python3 ./main.py -graph Li_6 6 50 10 3D &

python3 ./main.py -graph Li_7 6 50 10 3D &

python3 ./main.py -graph N_14 6 50 10 3D &

python3 ./main.py -graph N_15 6 50 10 3D &

python3 ./main.py -graph Na_23 6 50 10 3D &

python3 ./main.py -graph O_16 6 50 10 3D &

python3 ./main.py -graph O_17 6 50 10 3D &

python3 ./main.py -graph O_18 6 50 10 3D &

python3 ./main.py -graph Si_28 6 50 10 3D &

python3 ./main.py -graph Si_29 6 50 10 3D &

python3 ./main.py -graph Si_30 6 50 10 3D &

# # =======================================================================

echo "Done!"