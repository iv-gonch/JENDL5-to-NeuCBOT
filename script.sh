#!/bin/bash 

# max_MT =   {"Li_6" : 53, 
            # "Li_7" : 54, 
            # "Be_9" : 52, 
            # "B_10" : 54, 
            # "B_11" : 54, 
            # "C_12" : 50, 
            # "C_13" : 54, 
            # "N_14" : 54, 
            # "N_15" : 54, 
            # "O_17" : 53, 
            # "O_18" : 54, 
            # "F_19" : 77, 
            # "Na_23": 78}

# ============== file structure ============== #
# MT50 =  {"Li_6" : 50, 
        # "Li_7" : 50, 
        # "Be_9" : 50, 
        # "B_10" : 50, 
        # "B_11" : 50, 
        # "C_12" : 50, 
        # "C_13" : 50, 
        # "N_14" : 50, 
        # "N_15" : 50, 
        # "O_17" : 50, 
        # "O_18" : 50, 
        # "F_19" : 50, 
        # "Na_23": 50}

# MT51 =  {"Li_6" : 51, 
         # "Li_7" : 51, 
         # "Be_9" : 51, 
         # "B_10" : 51, 
         # "B_11" : 51, 
         # "C_13" : 51, 
         # "N_14" : 51, 
         # "N_15" : 51, 
         # "O_17" : 51, 
         # "O_18" : 51, 
         # "F_19" : 51, 
         # "Na_23": 51}

# MT52 =  {"Li_6" : 52, 
         # "Li_7" : 52, 
         # "Be_9" : 52, 
         # "B_10" : 52, 
         # "B_11" : 52, 
         # "C_13" : 52, 
         # "N_14" : 52, 
         # "N_15" : 52, 
         # "O_17" : 52, 
         # "O_18" : 52, 
         # "F_19" : 52, 
         # "Na_23": 52}

# MT53 =  {"Li_6" : 53, 
         # "Li_7" : 53, 
         # "B_10" : 53, 
         # "B_11" : 53, 
         # "C_13" : 53, 
         # "N_14" : 53, 
         # "N_15" : 53, 
         # "O_17" : 53, 
         # "O_18" : 53, 
         # "F_19" : 53, 
         # "Na_23": 53}

# MT54 =  {"Li_7" : 54, 
         # "B_10" : 54, 
         # "B_11" : 54, 
         # "C_13" : 54, 
         # "N_14" : 54, 
         # "N_15" : 54, 
         # "O_18" : 54, 
         # "F_19" : 54, 
         # "Na_23": 54}

# MT55-77={"F_19" : 55-77, 
         # "Na_23": 55-77}

# MT78 =  {"Na_23": 78}


# ============== start! ============== #

echo "Start!"; echo "" 

# ============== MT50 ============== #
python3 ./main.py -MT 50 -nucleus Li_6 &&
python3 ./main.py -MT 50 -nucleus Be_9 &&
python3 ./main.py -MT 50 -nucleus B_10 &&
python3 ./main.py -MT 50 -nucleus C_12 &&
python3 ./main.py -MT 50 -nucleus N_14 &&
python3 ./main.py -MT 50 -nucleus O_17 &&
python3 ./main.py -MT 50 -nucleus F_19 &&
python3 ./main.py -MT 50 -nucleus Na_23 &&

python3 ./main.py -MT 50 -nucleus Li_7 &&
python3 ./main.py -MT 50 -nucleus B_11 &&
python3 ./main.py -MT 50 -nucleus C_13 &&
python3 ./main.py -MT 50 -nucleus N_15 &&
python3 ./main.py -MT 50 -nucleus O_18 &&
# ============== end MT50 ============== #


# ============== MT51 ============== #
python3 ./main.py -MT 51 -nucleus Li_6 &&
python3 ./main.py -MT 51 -nucleus Be_9 &&
python3 ./main.py -MT 51 -nucleus B_10 &&
python3 ./main.py -MT 51 -nucleus N_14 &&
python3 ./main.py -MT 51 -nucleus O_17 &&
python3 ./main.py -MT 51 -nucleus F_19 &&
python3 ./main.py -MT 51 -nucleus Na_23 &&

python3 ./main.py -MT 51 -nucleus Li_7 &&
python3 ./main.py -MT 51 -nucleus B_11 &&
python3 ./main.py -MT 51 -nucleus C_13 &&
python3 ./main.py -MT 51 -nucleus N_15 &&
python3 ./main.py -MT 51 -nucleus O_18 &&
# ============== end MT51 ============== #


# ============== MT52 ============== #
python3 ./main.py -MT 52 -nucleus Li_6 &&
python3 ./main.py -MT 52 -nucleus Be_9 &&
python3 ./main.py -MT 52 -nucleus B_10 &&
python3 ./main.py -MT 52 -nucleus N_14 &&
python3 ./main.py -MT 52 -nucleus O_17 &&
python3 ./main.py -MT 52 -nucleus F_19 &&
python3 ./main.py -MT 52 -nucleus Na_23 &&

python3 ./main.py -MT 52 -nucleus Li_7 &&
python3 ./main.py -MT 52 -nucleus B_11 &&
python3 ./main.py -MT 52 -nucleus C_13 &&
python3 ./main.py -MT 52 -nucleus N_15 &&
python3 ./main.py -MT 52 -nucleus O_18 &&
# ============== end MT52 ============== #


# ============== MT53 ============== #
python3 ./main.py -MT 53 -nucleus Li_6 &&
python3 ./main.py -MT 53 -nucleus Be_9 &&
python3 ./main.py -MT 53 -nucleus B_10 &&
python3 ./main.py -MT 53 -nucleus N_14 &&
python3 ./main.py -MT 53 -nucleus O_17 &&
python3 ./main.py -MT 53 -nucleus F_19 &&
python3 ./main.py -MT 53 -nucleus Na_23 &&

python3 ./main.py -MT 53 -nucleus Li_7 &&
python3 ./main.py -MT 53 -nucleus B_11 &&
python3 ./main.py -MT 53 -nucleus C_13 &&
python3 ./main.py -MT 53 -nucleus N_15 &&
python3 ./main.py -MT 53 -nucleus O_18 &&
# ============== end MT53 ============== #


# ============== MT54 ============== #
python3 ./main.py -MT 54 -nucleus Be_9 &&
python3 ./main.py -MT 54 -nucleus B_10 &&
python3 ./main.py -MT 54 -nucleus N_14 &&
python3 ./main.py -MT 54 -nucleus F_19 &&
python3 ./main.py -MT 54 -nucleus Na_23 &&

python3 ./main.py -MT 54 -nucleus Li_7 &&
python3 ./main.py -MT 54 -nucleus B_11 &&
python3 ./main.py -MT 54 -nucleus C_13 &&
python3 ./main.py -MT 54 -nucleus N_15 &&
python3 ./main.py -MT 54 -nucleus O_18 &&
# ============== end MT54 ============== #


# ============== MT55 ============== #
python3 ./main.py -MT 55 -nucleus F_19 &&
python3 ./main.py -MT 55 -nucleus Na_23 &&
# ============== end MT55 ============== #


# ============== MT56 ============== #
python3 ./main.py -MT 56 -nucleus F_19 &&
python3 ./main.py -MT 56 -nucleus Na_23 &&
# ============== end MT56 ============== #


# ============== MT57 ============== #
python3 ./main.py -MT 57 -nucleus F_19 &&
python3 ./main.py -MT 57 -nucleus Na_23 &&
# ============== end MT57 ============== #


# ============== MT58 ============== #
python3 ./main.py -MT 58 -nucleus F_19 &&
python3 ./main.py -MT 58 -nucleus Na_23 &&
# ============== end MT58 ============== #


# ============== MT59 ============== #
python3 ./main.py -MT 59 -nucleus F_19 &&
python3 ./main.py -MT 59 -nucleus Na_23 &&
# ============== end MT59 ============== #


# ============== MT60 ============== #
python3 ./main.py -MT 60 -nucleus F_19 &&
python3 ./main.py -MT 60 -nucleus Na_23 &&
# ============== end MT60 ============== #


# ============== MT61 ============== #
python3 ./main.py -MT 61 -nucleus F_19 &&
python3 ./main.py -MT 61 -nucleus Na_23 &&
# ============== end MT61 ============== #


# ============== MT62 ============== #
python3 ./main.py -MT 62 -nucleus F_19 &&
python3 ./main.py -MT 62 -nucleus Na_23 &&
# ============== end MT62 ============== #


# ============== MT63 ============== #
python3 ./main.py -MT 63 -nucleus F_19 &&
python3 ./main.py -MT 63 -nucleus Na_23 &&
# ============== end MT63 ============== #


# ============== MT64 ============== #
python3 ./main.py -MT 64 -nucleus F_19 &&
python3 ./main.py -MT 64 -nucleus Na_23 &&
# ============== end MT64 ============== #


# ============== MT65 ============== #
python3 ./main.py -MT 65 -nucleus F_19 &&
python3 ./main.py -MT 65 -nucleus Na_23 &&
# ============== end MT65 ============== #


# ============== MT66 ============== #
python3 ./main.py -MT 66 -nucleus F_19 &&
python3 ./main.py -MT 66 -nucleus Na_23 &&
# ============== end MT66 ============== #


# ============== MT67 ============== #
python3 ./main.py -MT 67 -nucleus F_19 &&
python3 ./main.py -MT 67 -nucleus Na_23 &&
# ============== end MT67 ============== #


# ============== MT68 ============== #
python3 ./main.py -MT 68 -nucleus F_19 &&
python3 ./main.py -MT 68 -nucleus Na_23 &&
# ============== end MT68 ============== #


# ============== MT69 ============== #
python3 ./main.py -MT 69 -nucleus F_19 &&
python3 ./main.py -MT 69 -nucleus Na_23 &&
# ============== end MT69 ============== #


# ============== MT70 ============== #
python3 ./main.py -MT 70 -nucleus F_19 &&
python3 ./main.py -MT 70 -nucleus Na_23 &&
# ============== end MT71 ============== #


# ============== MT72 ============== #
python3 ./main.py -MT 72 -nucleus F_19 &&
python3 ./main.py -MT 72 -nucleus Na_23 &&
# ============== end MT72 ============== #


# ============== MT73 ============== #
python3 ./main.py -MT 73 -nucleus F_19 &&
python3 ./main.py -MT 73 -nucleus Na_23 &&
# ============== end MT73 ============== #


# ============== MT74 ============== #
python3 ./main.py -MT 74 -nucleus F_19 &&
python3 ./main.py -MT 74 -nucleus Na_23 &&
# ============== end MT74 ============== #


# ============== MT75 ============== #
python3 ./main.py -MT 75 -nucleus F_19 &&
python3 ./main.py -MT 75 -nucleus Na_23 &&
# ============== end MT75 ============== #


# ============== MT76 ============== #
python3 ./main.py -MT 76 -nucleus F_19 &&
python3 ./main.py -MT 76 -nucleus Na_23 &&
# ============== end MT76 ============== #


# ============== MT77 ============== #
python3 ./main.py -MT 77 -nucleus F_19 &&
python3 ./main.py -MT 77 -nucleus Na_23 &&
# ============== end MT77 ============== #


# ============== MT78 ============== #
python3 ./main.py -MT 78 -nucleus Na_23 &&
# ============== end MT78 ============== #

echo "Done!"; echo "" 