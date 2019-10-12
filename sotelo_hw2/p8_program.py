#!/usr/bin/env python3


#p8_program.py
#WRITE FILE - Creates a file containing two user provided strings.

#05Jul2019 Asis A Sotelo
 


import os 
import sys


string1 = input("Enter String 1:")

print()

string2 = input("Enter String 2:")

listOfStrings = [string1,string2]

fileOfUSER = input("Enter New File Name:")




print()

def carefule_write(outlines, filename):
	if os.access(filename, os.F_OK):
		print('\nOutput file already exists: %s\n\n' % filename, file =sys.stderr)
		return

	outfile = open(filename, 'w')
	for i in outlines:
		outfile.write('%s \n'% i)
	outfile.close()

carefule_write(listOfStrings,fileOfUSER)





