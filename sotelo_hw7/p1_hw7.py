#!/usr/bin/env python3
#
#
#p1_hw7.py - Fork() and Exec()
#
#Asis A Sotelo
#
#03Aug19
#
#

USAGE = """ A program that starts counting from one and prints the next number ever half second. After reaching a multiple of ten it will fork, the child will then announce it will execute ls and then execute 'ls -l'

		"""

import os 
import time

mypid = os.getpid()

while True:

	for i in range(1,11,1):
		print(i)
		time.sleep(.5)
	print("About to Fork . . .")
	time.sleep(.3)
	retval = os.fork()
	child = (retval ==0)
	if child:
		mypid=os.getpid()
		print("I am the child pid: %d  about to execute ls" %mypid)
		os.execv('/bin/echo',['','-l'])
		time.sleep(.5)
	else:
		time.sleep(.5)



time.sleep(.5)




