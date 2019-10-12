#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Asis A Sotelo
#Problem 7 Execution Speed
#11Jul2019
#p7_h3.py


import time

N = 10000

t0 = time.perf_counter()

for i in range(N):
   pass

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for %d loops: %.16f s' % (N, elapsed))
print()


# Two float variables

v=4.5
u = 43.4
t0 = time.perf_counter()

for i in range(N):
   v + u

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for addition of two float variables:%.16f s' % elapsed)
print()

# Multiplication of two float variables

t0 = time.perf_counter()

for i in range(N):
   v*u

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for multiplication of two float variables:%.16f s' % elapsed)
print()


#Integer division of two variables


h = int(5)
g = int(10)
t0 = time.perf_counter()

for i in range(N):
   g/h

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for division of two integer variables:%.16f s' % elapsed)
print()

# Appending increasing list 

listcheck = []

t0 = time.perf_counter()
for i in range(N):
   
    listcheck.append(2)

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for appending to an increasing list: %.16f s' % elapsed)
print()


#Appending list that made smaller eachtime

t0 = time.perf_counter()

for i in range(N):
    
    
    listcheck.append(2)

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for appending with length of list eliminated: %.16f s' % elapsed)
print()

print("THIS DOES NOT MATTER THE LENGTH OF THE LIST")

def does_nothin():
    
    """This funcgion does nothing"""
    pass


t0 = time.perf_counter()

for i in range(N):
   
    does_nothin()

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for a call to function that does nothing: %.16f s' % elapsed)
print()    

def adds_two(x,y):
    
    """This equation adds two float variables"""
    
    x+y
    

f=4.565
a=23.345


t0 = time.perf_counter()

for i in range(N):
   
    adds_two(f,a)

elapsed = (time.perf_counter() - t0)/N

print()
print('Time elapsed for function that adds two float variables: %.16f s' % elapsed)
print()



