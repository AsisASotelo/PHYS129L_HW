#!/usr/bin/env python3
#
#p3_hw7.py - Coin Simulation
#
#Asis A Sotelo	
#
#

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random as rng
import scipy.stats as stats

def toss(numoftosses):
	
	toss_array = []
	
	
	x = rng(numoftosses)
	heads = (x<.5)
	heads = np.sum(heads)
	return heads

plot_arr = np.zeros(1000)

for i in range(1000):
	x = toss(100)
	plot_arr[i] = x

meanx = np.mean(plot_arr)
minx = np.max(plot_arr)

def gauss(N,p,x):
	
	q = 1-p
	mu = N*p
	sigma = np.sqrt(N*p*q)
	
	coeff = (1/(sigma * np.sqrt(2*np.pi)))
	expo  = np.exp(-np.square(x - mu) * (1/(2*np.square(sigma))))

	
	return coeff * expo
p=.5
N=100
q=1-p
mu = N*p
sigma = np.sqrt(N*p*q)

xvals = np.linspace(mu - 3*sigma, mu +3*sigma,100)

plt.figure()

plt.hist(plot_arr,normed=True)
plt.plot(xvals, gauss(N,p,xvals))


plt.show()
plt.savefig('wind_si.eps',format='eps')
