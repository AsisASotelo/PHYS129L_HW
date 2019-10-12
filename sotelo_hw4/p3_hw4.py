#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#p3_hw3.py
#Wind Speed 
#17Jul2019

import numpy as np
import matplotlib.pyplot as plt


datafiles= np.loadtxt('/home/pi/physrpi/coursefiles/wind.dat')

wind_data =datafiles.T

xmar = int(abs((wind_data[0][-1] - wind_data[0][0])/6))
ymar = int(abs(max(wind_data[1])/4))

print(xmar)
print(ymar)

f1, ax1 = plt.subplots()


## THE FOLLOWING SETS THE AXIS LABELS AND TITLE OF GRAPH
ax1.set_xlabel("Time of Day in Hours")
ax1.set_ylabel("Speed of Wind [Knots]")
ax1.set_title("Wind Speed Vs. Time of Day")

## SETS TICKS LABEL AND FONT AS WELL AS ERROR BARS 


ax1.set_xlim(wind_data[0][0]-xmar, wind_data[0][-1]+xmar)
ax1.set_ylim(0,max(wind_data[1])+ymar)
#ax1.plot(wind_data[0], wind_data[1], 'o')
ax1.errorbar(wind_data[0],wind_data[1],yerr=wind_data[2],fmt='o', capsize=3)

f1.show()

## SAVES THE FIGURE TO AN .EPS FILE

plt.savefig("wind_data.eps")

print(wind_data)
print(type(wind_data))


