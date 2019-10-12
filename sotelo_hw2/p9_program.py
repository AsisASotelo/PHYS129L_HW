#!/usr/bin/env python3

#PROBLEM9-READ FILE AND AVERAGE
#05JUL2019 ASIS A SOTELO
#Reads number from a user specified file and prints out average. File must contain one number per line

import os
import sys
import math
import subprocess


def file_readlines(filename):

	infile = open(filename, 'r')
	inlines = infile.readlines()
	infile.close()
	return(inlines)

user_file = input("Enter File Name:\n")
print()

numbers = (file_readlines(user_file))

print(type(numbers))
print(type(numbers[0]))


[float(i) for i in numbers]	







