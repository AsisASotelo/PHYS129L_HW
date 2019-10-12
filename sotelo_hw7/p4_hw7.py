#!/usr/bin/env python3
#
#p4_hw7.py - Counting Simulation
#
#Asis A Sotelo
#

USAGE = """ Simulates photon counting"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng
import datetime as datetime

def factorial(n):
	val = 0
	if n == 1:
		return n 
	else:
		return n*factorial(n-1)
print("check1")
def detect():
	count = 0
	for i in range(1000):
		x = rng(1000)
		photon  = x< .002
	detect = sum(photon)
	
	return detect
print("check2")
plot_arr=np.zeros(1000)
for i in range(1000):
	y = detect()
	plot_arr[i] = y

print(len(plot_arr))	
