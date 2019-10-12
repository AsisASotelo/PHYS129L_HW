#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Asis A Sotelo
#PRIME FACTORIZATION OF A NUMBER
#11Jul2019
#p5_hw3.py


import sys
import math
import numpy as np
print()

while True:
    instr = input("Please enter an integer: ")
    try:
       num = int(instr)
    except ValueError:
       print("Your input was not an integer.  Try again.\n", file=sys.stderr)
    else:
       break


def prime_factors(n):
    
    """Returns the prime numbers of a number"""
    
    #First checks to see if number is even then repeats as long as the number 
    #Contains more factors of 2
    
    
    while n % 2 ==0:
        print(2)
        n=n/2
        
    # Create a loop that divides each number i into the number until it finds 
    # a factor which it then prints and divides the number
    
        
    for i in range(3,int(math.sqrt(n)),2):
        while n % i == 0:
            print(i)
            n=n/i
            
    # Once it exits if number is greater than two it is a prime number that 
    # cannot be further divisable by a number so it prints 
    if n>2:
        print(n)
        
        
prime_factors(num)
        
        
        
        
        
        
        
        
        
        
    
        
        
        


