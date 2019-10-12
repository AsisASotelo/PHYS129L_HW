#!/usr/bin/env python3
#
#
#p4_hw6.py - Acquire and Store Data
#
#Asis A Sotelo
#
#24Jul19 Created Program
#
#

""" Program that acqures one second of voltages from solar cell at arate of 920 samples per second"

"""


ACQTIME = 1.0 # Seconds of Data Acquisition set to 1 second 

# SAMPLES PER SECOND
# options: 128, 250, 512, 1024, 2048, 4096, 6144.

SPS = 920 # This setting is to 920 samples per second

# FULL-SCale Range in mV
# options: 256, 512, 1024, 2048, 4096, 6144.

VRANGE = 4096

nsamples = int(ACQTIME*SPS) # Sets number of samples to 920 samples in int
sinterval = 1.0/SPS #Sets the interval length

import sys 
import time
import numpy as np
import matplotlib.pyplot as plt


from Adafruit import ADS1x15

##########################################################################

indata = np.zeros(nsamples,'float') # Creates array for our data 

print()
print("Initializing ADC ... ")
print()

#Default ADC IC is ADS1015
#Defalut address is 0x48 on the default I2C bus

adc=ADS1x15()




# First two arguments are the channels
# Third argument is the full-scale range in mV (default +/- 6144).
#    options: 256, 512, 1024, 2048, 4096, 6144.
#    Note: input should not exceed VDD + 0.3
# Fourth argument is samples per second (default 250).
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
#


adc.startContinuousDifferentialConversion(2,3,pga=VRANGE, sps=SPS)

input('Press <Enter> to start %.1f s data acquisition ...'% ACQTIME)
print()
t0 = time.perf_counter()

for i in range(nsamples):
	st = time.perf_counter()
	indata[i] = .001*adc.getLastConversionResults()
	while(time.perf_counter() - st) <= sinterval:
		pass
t = time.perf_counter() - t0

adc.stopContinuousConversion()

file= open('p4_data1.txt',"w+")

for i in range(len(indata)):

    file.write("%.5f\n" % indata[i])

file.close()

print("Created Text file 'p4_data.txt'")


xpoints = np.arange(0, ACQTIME, sinterval)
print('Time Elapsed : %.9f s.' % t)
f1, ax1 = plt.subplots()

ax1.plot(xpoints,indata,'-',drawstyle='steps-post')

plt.savefig("p4_figure.eps")

f1.show()


 



input("\nPress <Enter> to exit .. \n")

