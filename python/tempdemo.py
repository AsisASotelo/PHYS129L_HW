#!/usr/bin/env python3
#
# tempdemo.py - Temperature measurement demo with MCP9808
#
# 18May16  Adapted from Adafruit code by Everett Lipman
#

import time

#
# Adafruit libraries modified by Ben Laroque for Python 3
#
import Adafruit.MCP9808 as MCP9808
##############################################################################

def cel2far(T):
   """Convert T from Celsius to Fahrenheit
   """
   return(1.8*T + 32.0)
##############################################################################

#
# Default address is 0x18, on default I2C bus.
#
# Alternative: MCP9808(address=0x??, busnum=N).
#
sensor = MCP9808()

sensor.begin()

while True:
   Tc = sensor.readTempC()  # returns float
   Tf = cel2far(Tc)
   print('%.4f degC  %.4f degF' % (Tc, Tf))
   time.sleep(0.5)
