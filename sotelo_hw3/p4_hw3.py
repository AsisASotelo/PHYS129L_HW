#!/usr/bin/env python3

#Asis A Sotelo
#PRIME FACTORIZATION OF A NUMBER
#11Jul2019


import numpy as np


data_file = "classlist.csv"
data_set = np.genfromtxt(data_file,dtype='str',delimiter=',')


for i in range(len(data_set)):
    print("Happy Valentine's Day, %s %s!" \
    % (data_set[i][1].title(), data_set[i]\
    [0].title()))
