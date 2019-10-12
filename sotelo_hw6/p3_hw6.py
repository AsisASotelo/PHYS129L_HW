#!/usr/bin/env python3
#
#p3_hw6.py
#
#Temperature Stripchart
#
#25Jul19 Created Program
#
#
"""

Modification of the stripchart.py program to produce running plot from temperature sensor MCP9808

"""


import Adafruit.MCP9808 as MCP9808 # Added this import line from tempdemo.py
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


# Define sensor MCP9808

sensor = MCP9808()
sensor.begin()

class Scope(object):
	def __init__(self,ax,maxt=2,dt=.001,maxy=50,miny = 30):
		self.ax = ax
		self.dt = dt
		self.miny=miny
		self.maxy = maxy
		self.maxt = maxt
		self.tdata = np.array([])
		self.ydata = np.array([])
		self.t0 = time.perf_counter()
		self.line = Line2D(self.tdata, self.ydata)
		self.ax.add_line(self.line)
		self.ax.set_ylim(self.miny,self.maxy)
		self.ax.set_xlim(0,self.maxt)
		
		

	def update(self,data):
		t,y= data 
		self.tdata = np.append(self.tdata, t)
		self.ydata = np.append(self.ydata, y)
		self.ydata = self.ydata[self.tdata > (t-self.maxt)]
		self.tdata = self.tdata[self.tdata > (t-self.maxt)]
		self.ax.set_ylim(self.ydata[0]-2,self.ydata[0]+2) #Keeps graph on sensor
		self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
		self.ax.figure.canvas.draw()
		self.line.set_data(self.tdata,self.ydata)
		return self.line,
	
	def emitter(self, p = 0.1):
		while True:
			t = time.perf_counter()- self.t0
			v = sensor.readTempC()
			
			yield t, v
			#if v> p:
			#	yield t, 0.
			#else:
			#	yield t, np.random.rand(1)

if __name__ == '__main__':
	dt = .001
	fig, ax = plt.subplots()
	fig.suptitle("Temp vs Time")
	plt.xlabel("Time [s]")
	plt.ylabel("Temperature [C]")
	scope =Scope( ax,maxt= 10, dt=dt)
	ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval= dt*100., blit = True)


	plt.show()
