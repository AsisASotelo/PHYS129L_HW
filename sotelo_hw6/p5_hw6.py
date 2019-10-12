#!/usr/bin/env python3
#
#
#p5_hw6.py Fourier Analysis
#
#Asis A Sotelo 
#
#24Jul19 Created Program
#

import numpy as np 
import matplotlib.pyplot as plt



# Data Import
data = np.loadtxt('p5_data.txt') # Import Data<-- 920 Samples

#NOTE: Before you transform the data you must eliminate the DC offset otherwise you will get a single spike at 0Hz. Take the mean of the data and subtract it from every element

data=data - np.mean(data)



# Fourier Transform Using numpy.fft.fft
ft = np.fft.fft(data, n =920) # << Set length of axis to size of data



# Absolute Value of transform
ftabs = np.abs(ft)



# Power Spectrum (ps) - The square of the Fourier Transform
ps = ftabs ** 2

# Xvalues are created by taking all of the frequences until f = 0,1,2,...920 in range of len(data)

xvals = np.fft.fftfreq(len(ps),1.0/920)
f1,fig = plt.subplots()
fig.set_xlim(0,200) #My lightbulb operated at a frequency of 120Hz
fig.plot(xvals,ps)
f1.show()

input("Press <Enter> to Exit...")

