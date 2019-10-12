#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#p9_hw4.py

#18Jul2019


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm



fig = plt.figure()
ax = Axes3D(fig)
X = np.linspace(0,2*2.5*np.pi,501)
Y = np.linspace(0,2.5*2*np.pi,501)

X,Y = np.meshgrid(Y,X)
Z = np.cos(Y) * np.sin(X)
ax.plot_surface(X,Y,Z, cmap =cm.coolwarm , linewidth = 0, antialiased = False)

plt.show
fig.savefig('surface_plot.eps')