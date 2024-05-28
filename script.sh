#!/bin/bash

echo "Start!"

# python3 ./main.py -nucleus Li_6 &&
# python3 ./main.py -nucleus Li_7 &&


python3 ./main.py -nucleus Be_9 &&

python3 ./main.py -nucleus B_10 &&    # No mass in chemistry.py
python3 ./main.py -nucleus B_11 &&

python3 ./main.py -nucleus C_12 &&
python3 ./main.py -nucleus C_13 &&

# python3 ./main.py -nucleus N_14 &&
# python3 ./main.py -nucleus N_15 &&

python3 ./main.py -nucleus O_16 &&      # No JENDL data
# python3 ./main.py -nucleus O_17 &&
# python3 ./main.py -nucleus O_18 &&

# python3 ./main.py -nucleus F_19 &&


# python3 ./main.py -nucleus Na_23 &&


python3 ./main.py -nucleus Al_27 &&     # No JENDL data

python3 ./main.py -nucleus Si_28 &&     # No JENDL data
python3 ./main.py -nucleus Si_29 &&     # No JENDL data
python3 ./main.py -nucleus Si_30 &&     # No JENDL data

echo "Done!"