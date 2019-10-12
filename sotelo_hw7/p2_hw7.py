#!/usr/bin/env python3
#
#p2_hw6.py
#
#StripChart
#
#25Jul19
#
#
"""

Modification of the stripchart.py program to produce running plot of sin(wt)
vs. t, with w= pi rad/s

"""



import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import sys
import threading

global glob

glob =30

class Scope(object):
	def __init__(self,ax,maxt=2,dt=.001,maxy = 50, miny = 30):
		self.ax       = ax
		self.dt       = dt
		self.miny     = miny
		self.maxy     = maxy 
		self.maxt     = maxt
		self.tdata    = np.array([])
		self.ydata    = np.array([])
		self.t0       = time.perf_counter()
		self.line     = Line2D(self.tdata, self.ydata)
		
		

		self.ax.add_line(self.line)
		self.ax.set_ylim(self.miny,self.maxy)
		self.ax.set_xlim(0,self.maxt)

	def update(self,data):
		t,y= data 
		self.tdata = np.append(self.tdata, t)
		self.ydata = np.append(self.ydata, y)
		self.ydata = self.ydata[self.tdata > (t-self.maxt)]
		self.tdata = self.tdata[self.tdata > (t-self.maxt)]
		
		self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
		self.ax.set_ylim(0,100 )
		self.ax.figure.canvas.draw()
		self.line.set_data(self.tdata,self.ydata)
		return self.line,
	
	def emitter(self, p = 0.1):
		while True:
			t = time.perf_counter()- self.t0
			v = glob
			
			yield t, v
			#if v> p:
			#	yield t, 0.
			#else:
			#	yield t, np.random.rand(1)

def thethread():
	global glob
	while True:

		instr = input("Please enter an integer:")
		try:
			n= int(instr)
			glob =n
		except ValueError:
			print("Your input was not an integer. Try again\n", file=sys.stderr)
	
		




if __name__ == '__main__':
    
    dt = 0.001
    fig,ax = plt.subplots()
    thr1 = threading.Thread(target = thethread)
    thr1.start() 
    scope = Scope(ax,maxt=10, dt = dt)
    ani = animation.FuncAnimation(fig,scope.update,scope.emitter,interval = dt*100, blit = True)
    plt.show()
   










