#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Asis A Sotelo
#FIBONNACI NUMBERS
#11Jul2019
#p8_h3.py


import sys
import math
import numpy as np
print()

while True:
    instr = int(input("Please enter an integer: "))
    
    if 0<instr<76:
        
        try:
            
            num = int(instr)
        except ValueError:
                print("Your input was not an integer or less than zero or greater than 75.  Try again.\n", file=sys.stderr)
        else:
            break
        
        
count = 0

count_add = 1

print(count)

print(count_add)
for i in range(instr):
    
    counttot = count + count_add
    print(counttot)
    count = count_add
    count_add = counttot
   
    
    