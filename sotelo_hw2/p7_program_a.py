#!/usr/bin/env python3 
#
#p7_program_a.py

#05jul2019 Asis A Sotelo

# This program uses subprocess module to and prints out once per second in infinite loop

import subprocess
import time
import math

print() ## This clears the input buffer

#
#

output_temp = subprocess.check_output(['cat','/sys/class/thermal/thermal_zone0/temp'],universal_newlines =True)

new_temp = (float(output_temp))/1000.0


while True:
	output_temp = subprocess.check_output(['cat','/sys/class/thermal/thermal_zone0/temp'],universal_newlines =True)
	new_temp = (float(output_temp))/1000.0
	time.sleep(1)
	print(new_temp)
