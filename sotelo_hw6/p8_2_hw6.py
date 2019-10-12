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

"""
Graphs the fractional error Xerr/Xact in the determined value of pi as a function of N where N is the number of randomly generated points.


"""

### We will import libraries for numpy, matplotlib, and Scipy###
import sys
from numpy.random import random as rng
import matplotlib.pyplot as plt
import numpy as np

########  Makes sure input is an integer between a certain range[]  ############


#########################################################################

# Following Creates User Specified N number of Uniformly Dist. Points #

N = (1, 100, 250, 500, 1000, 10000,100000)
approx = np.zeros(len(N))
for j in range(len(N)):

	x_arr = rng(N[j])*2
	y_arr = rng(N[j])*2
	
	hyp = np.square(x_arr-1) + np.square(y_arr-1)
	usr_num = N
	count = 0
	for i in range(1,usr_num[j]):
	
		if hyp[i] <= 1:
			count+=1
	piapprox = (4*count)/ usr_num[j]
	approx[j] = piapprox
	
array_approx = (abs(approx-np.pi)/np.pi) * 100




plt.plot(N,array_approx)

plt.savefig("p8_plot.eps")	
plt.show()  











