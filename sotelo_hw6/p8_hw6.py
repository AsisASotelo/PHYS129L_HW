#!/usr/bin/env python3
#
#p8_hw6.py - Monte Carlo Circle 
#
#Asis A Sotelo
#
#24Jul19 Created Program
#
#
#

""" A. Writes a program that generates a user - specified number N of 
		Uniformly distributed random poins on the x-y plane with x and
			y both running from 0-2

"""

### We will import libraries for numpy, matplotlib, and Scipy###
import sys
from numpy.random import random as rng
import matplotlib.pyplot as plt
import numpy as np

########  Makes sure input is an integer between a certain range[]  ############


while True:

    usr_num = (input("Enter a positive integer: \n"))

    try:
        usr_num = int(usr_num)
        if usr_num < 0:
            raise ValueError()
    except ValueError:
        print("Your input was not an integer or between 4 and 10 Try Again.\n", file= sys.stderr)
    else:
        break


#########################################################################

# Following Creates User Specified N number of Uniformly Dist. Points #

arr_x = (rng(usr_num)*2)
arr_y = (rng(usr_num)*2)

hyp =(np.square(arr_x-1) + np.square(arr_y-1))  


count = 0
for i in range(0,usr_num):
	
	if hyp[i] <= 1:
		count +=1

 


print("The approximation of pi with %d points is:" % usr_num)
print((4*count)/usr_num)











