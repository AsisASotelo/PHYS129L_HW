#!/usr/bin/env python3
#
#p6_hw7.py - Numerical Integration
#
#03Aug19 Asis A Sotelo
#


import numpy as np
import scipy 
import random
from numpy.random import random as rng

## TWO METHODS 

## METHOD A - Adding A Lot of Rectangles

def expo(x):
	return np.exp(-np.square(inter))


def monte():
	
	numsteps = 1000
	xmin = -10 
	xmax = 10

	ymin = (expo(xmin))
	ymax = (expo(xmax))

	for i in range(numsteps):
		x = xmin + (xmax - xmin) * float(i)/numsteps
		y= expo(x)
		if y <ymin:
			ymin =y 
		if y> ymax:
			ymax = y

rectArea = (xmax - xmin) *(ymax - ymin)
numPoints = 100000

counter = 0

for j in range(numPoints):
	
	x = xmin +(xmax -xmin) * random.random()
	y = ymin +(ymax -ymin) * random.random()

	if expo(x) > 
	
		
	return scale *tot

print(monte())
	

