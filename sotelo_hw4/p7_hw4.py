#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#p7_hw4.py

#18Jul2019

#MANDELBROT
import numpy as np
import matplotlib.pyplot as plt
import sys
#
# image size
#
X = 512
Y =384

#
# array for image data (pixel values): one integer value at each (x,y) point
#
# color is determined from pixel value by the colormap
#
pvals = np.zeros((X,Y), dtype='uint')

#xinc = 1000/X
#yinc = 1000/Y
MAX_ITERATION = 250


# THE FULL MANDELBROT SET IS X [-2,2] Y  [-1,1]
real_start= -1.41
real_end = -1.38
imaginary_start = .0068
imaginary_end = -.0068

### DEFINE THE FUNCTION

def mandelbrot(x,y,maxiter):
    
    
    ##THESE ARE THE LOCAL VALUES FOR C AN Z
    z = complex(0,0)
    c = complex(x,y)
    
    for iterations in range(maxiter):
        
        z= z**2 + c
        
        if abs(z) > 2:
            return iterations
        
    return 0


def progress(count,total,status = ''):
    
    bar_len = 60
    filled_len = int(round(bar_len*count/float(total)))
    
    
    bar = '=' * filled_len + '-' *(bar_len-filled_len)
    
    percents = round(100.0*count/float(total),1)
    
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar,percents,'%',status))
    sys.stdout.flush()
    
    
    
    
    
    
#
# Note that arrays are typically indexed using entriesside = 10
#x0 = (29*X)//32 - side
#x1 = (29*X)//32 + side
#y0 = (17*Y)//20 - side
#y1 = (17*Y)//20 + side
#pvals[x0:x1, y0:y1] = 0
# (i,j), where i is the row (vertical) and j is the column
# (horizontal).  This is different from addressing points
# (x,y) in the plane, where x, the first variable, indicates
# horizontal position, and y, the second, indicates vertical
# position.  To make i correspond with x and j with y, we
# will transpose the pvals m i*xinc + j*yincatrix below before displaying it.
# Furthermore, it is customary in raster graphics for the
# vertical dimension to increase downward from the upper
# left-hand corner of the screen, while in typical x,y plots
# the vertical dimension increases upward from the origin
# at the lower left.  So we also flip the entries along
# the vertical axis using np.flipud() before displaying.
# This way the pixels (i,j) we assign in the array correspond
# to the way we typically think of points in the x,y plane.
#
for j in range(Y):
    
    progress(j,Y)
    
    
    for i in range(X):
       pvals[i,j] = mandelbrot(real_start + (i/X)*(real_end - real_start), \
            imaginary_start + (j/Y)*(imaginary_end - imaginary_start),\
            MAX_ITERATION)

#
# example: set some pixels to zero:
#
#side = 10
#x0 = (29*X)//32 - side
#x1 = (29*X)//32 + side
#y0 = (17*Y)//20 - side
#y1 = (17*Y)//20 + side
#pvals[x0:x1, y0:y1] = 0

#
# Transpose and flip rows so that origin is displayed at bottom left,
# with x horizontal and y vertical.
#
# Note: changing pvals later WILL change plotarr!  plotarr is a
# different 'view' of the same data.
#
plotarr = np.flipud(pvals.transpose())

f1, ax1 = plt.subplots()

#
# interpolation='none' shows unaltered pixels at all scales
#
picture = ax1.imshow(plotarr, interpolation='none', cmap='jet')

#
# turn off axis labels
#
ax1.axis('off')

plt.savefig('mandel.ps')
# draw figure
#
f1.show()

