#!/usr/bin/env python3
#
#p6_hw6.py - Heat Transfer
#
#Asis A Sotelo
#
#24Jul19 Created Program
#
#

""" Modification of p5_hw6.py and p6_h6.py, acquires and saves temp data from MCP9808 @ 4samples/s

"""

import Adafruit.MCP9808 as MCP9808 # Import temperature sensor module
import numpy as np
import matplotlib.pyplot as plt
import time

### Define "sensor" as MCP9808()

sensor = MCP9808()
sensor.begin()

### Set Data Acquisition time

ACQTIME = 10.0

### Set samples Per Second 

SPS = 4

### Create sample interval and number of sample variables

nsamples = int(ACQTIME * SPS)
sinterval = 1.0/SPS

### Data array to be populated by samples 

indata = np.zeros(nsamples,'float')

print()
input('Press <Enter> to start %.1f s data acquisition ...' % ACQTIME)
print()

t0 = time.perf_counter()


### LOOP to read data to the indata array for n number of samples 

for i in range(nsamples):

	st = time.perf_counter()
	indata[i] = sensor.readTempC()
	while(time.perf_counter()-st) <=sinterval:
		pass
t=time.perf_counter() - t0

### Write data to file "p6_data.txt"

file = open('p6_data.txt','w+')

for i in range(len(indata)):
	file.write('%.5f\n' % indata[i])
	
file.close()

print("Created p6_data.txt")

#### Create the graph of the data 

xpoints = np.arange(0,ACQTIME,sinterval)

f1,ax1 = plt.subplots()
ax1.plot(xpoints, indata, 'o')
f1.show()

input("Press <Enter> to Exit...")




