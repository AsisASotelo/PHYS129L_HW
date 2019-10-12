#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#p6_hw4.py
#3-4-5 RIGHT TRIANGLE 
#17Jul2019

# IMAGE SIZE


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

X = 512
Y = 409


linw = 20
offset = 48







# 
#LETS NOT THAT AN ARRAY FOR IMAGE DATA IS FORMATTEd
#
#(pixelvalues): x,y,color[0:2]
#
#Where color is (r,g,b)
#
#Color is specified using an 8-bit unsigned integer(0-255)
#

#CREATE THE ARRAY OF PIXELS OF THE FIGURE USING VALUES DEFINED X,Y

pvals= np.zeros((X,Y,3), dtype= 'uint8')





        


for j in range(20):
    for i in range(400):
        pvals[i,j,0] = 0
        pvals[i,j,1] = 0
        pvals[i+offset+20,int(i*(3/4))+offset+j,2] = 255

for j in range(300):
    for i in range(linw):
        pvals[i,j,0] = 0
        pvals[i,j,1] = 0
        pvals[i+offset + 400,j+offset,2] = 255


for j in range(20):
    for i in range(400):
        pvals[i,j,0] = 0
        pvals[i,j,1] = 0
        pvals[i+offset+20,j+offset,2] = 255





plotarr = np.flipud(pvals.transpose(1,0,2))

f1, ax1 = plt.subplots()

# interpolation='none' shows unaltered pixels at all scales
#
picture = ax1.imshow(plotarr, interpolation='none')

#
# turn off axis labels
#
ax1.axis('off')

#
# draw figure
#
f1.show()
print(pvals)