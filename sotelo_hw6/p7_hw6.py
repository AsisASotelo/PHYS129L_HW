#!/usr/bin/env python3
#
#
#p7_hw6.py - Polynomial Fits
#
#Asis A Sotelo
#
#24Jul19 Created Program
#
#

""" Writes a program that generates user-specified number N of uniformly dist. random poings on a region of the x-y plane from 0-100. Then fits the set points using polynomial fits of degree 1(line), N-3, and N-1.

"""

### We will import libraries for numpy, matplotlib, and Scipy###
import sys
from numpy.random import random as rng
import matplotlib.pyplot as plt
import numpy as np

########  Makes sure input is an integer between a certain range[]  ############


while True:

	usr_num = (input("Enter a positive number between 4 < 11\n"))
	
	try:
		usr_num = int(usr_num)
		if usr_num < 0 or usr_num >= 10:
			raise ValueError()
	except ValueError:
		print("Your input was not an integer or between 4 and 10 Try Again.\n", file= sys.stderr)
	else:
		break



################################################################################

arr_x = (rng(usr_num)*100)
arr_y = (rng(usr_num)*100)

coeff_1 = np.polyfit(arr_x,arr_y,1)
equat_1 = np.poly1d(coeff_1)

coeff_N1 = np.polyfit(arr_x,arr_y,usr_num - 1 )
equat_N1 = np.poly1d(coeff_N1)

coeff_N3 = np.polyfit(arr_x,arr_y,usr_num -3)
equat_N3 = np.poly1d(coeff_N3)




x_fit_1 = np.linspace(0,100,100)
y_fit_1 = equat_1(x_fit_1)

x_fit_N3 = np.linspace (0,100,100)
y_fit_N3 = equat_N3(x_fit_N3)

x_fit_N1 = np.linspace (0,100,100)
y_fit_N1 = equat_N1(x_fit_N1)




plt.plot(arr_x,arr_y,'ro')

plt.plot(x_fit_1,y_fit_1, label = "Curve Fit Degree 1")
plt.plot(x_fit_N1,y_fit_N1, label = "Curve Fit Degree N-1")
plt.plot(x_fit_N3,y_fit_N3,label = "Curve Fit Degree N-3")
plt.legend()
plt.xlim(0,100)

plt.ylim(0,100)
plt.savefig("p7_hw6.eps", format = 'eps', dpi =1000)
plt.show()

