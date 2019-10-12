#!/usr/bin/python3
#
#
#
# Asis A Sotelo
#
# August 27

import numpy as np 

def sigmoid(x):
	return 1/ (1+np.exp(-x))

training_inputs = np.array([[0,0,1], [1,1,1], [1,0,1]
