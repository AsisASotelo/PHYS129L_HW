#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Asis A Sotelo
#SINE FUNCTION
#11Jul2019
#p9_hw3.py
import sys
import math


while True:
    instr = float((input("Please enter a non zero angle in degrees:\n")))
    
    if 0<instr<360:
        
        break
        
    else:
            print("Your number was not a non zero angle in degrees, try again.\n")

while True:
    instr1 = int(input("Pleae enter an integer value for the number of terms in series:\n"))
    
    if 0<instr1<26:
        
        break
        
    else:
            print("Your number was not a number between 0 and 25, try again.\n")
           
        
        
def sind(degrees, size):
    deg = (degrees % 360 )
    rad = deg * (math.pi/180)
    
    sine = []
    sine.append(rad)
    factorial = 2
    
    
    for i in range(1,size):
        sign = (-1)**(i)
        
        
        
        factorial = factorial * ((2*i) + 1)
        
        facto= ((2*i) +1)
     
        
        print(sine)
        radadd = ((rad ** (facto) ) / factorial) *sign
        
    
        sine.append(radadd)
       
    return(sum(sine))
        
    
print("The value of sin (%d) is : %.3f "% (instr , (sind(instr,instr1))))