#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#Plot Trig Functions
#p9_hw4

#18Jul2019





import numpy as np
import math as mat
import matplotlib.pyplot as plt


# DEFINES AN ARRAY THETA FOR THE X-AXIS

theta = np.linspace(0,(360) *2.5,51)

y1 = np.cos((theta/360)*2*mat.pi)
y2 = np.sin((theta/360)*2*mat.pi)


## CREATES A LIST FOR THE AXIS TICKS 

loc = (0,180,360,180*3,360*2,180*5)
lab = ("0$^\circ$", "180$^\circ$", "360$^\circ$", "540$^\circ$", "720$^\circ$", "900$^\circ$")
plt.xticks(loc,lab)

##CREATES THE LABELS AND THE TITLE OF THE GRAPH

plt.ylabel(r"f(${\theta}$)")
plt.xlabel(r"Theta in Degrees (${\theta ^\circ}$)")
plt.title("Sine and Cos vs Theta, 2.5 Period")
plt.plot(theta,y1,label = r"cos ${\theta^\circ}$")
plt.plot(theta,y2, label = r"sin ${\theta^\circ}$")


## PLOTS THE GRAPH AND CREATES A LEGEND


plt.legend()

plt.show()
