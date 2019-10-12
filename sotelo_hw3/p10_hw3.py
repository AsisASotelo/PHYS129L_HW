#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Asis A Sotelo
#PRIME FACTORIZATION OF A NUMBER
#11Jul2019
#p5_hw3.py




import sys
import math
import numpy as np
import time 




def in_date():

    while True:
    
    
    
        date = str(input("Please enter the date in the following format 'DDMmmYYYY'\n"))
    
        try:
            date_real = time.strptime(date,'%d%b%Y')
        
        except ValueError:
        
            print("Your input did not match the format. Try again.", file = sys.stderr)
            
        else: 
            
            print("\n The date entered is: %s \n" % date)
        
            return(date_real)

    
    


def julian_day(caldate):
    
    
    Y = caldate.tm_year
    M = caldate.tm_mon 
    A = math.floor(Y/100)
    B = 2 - A + int(A/4)
    D = caldate.tm_mday
    if M < 3 :
        
        julian_date = math.floor(365.25*((Y-1)+4716)) + math.floor(30.6001*((M+12)+1)) + D + B - 1524.5
        
        print("The date entered corresponds to julian date %f \n" % julian_date)
        return julian_date
        
    else:
        
        julian_date = math.floor(365.25*((Y)+4716)) + math.floor(30.6001*((M)+1)) + D + B - 1524.5
        
        
    print("The date entered corresponds to julian date %f \n" % julian_date)
    return julian_date
    
    
    
def julian_weekday(day):
    
    day_of_week = int((day + 1.5) % 7)
    list_of_days = ["Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    
    print("The day of the week is %s" % list_of_days[day_of_week-1])
    
    print(day_of_week)
    return(day_of_week)
    
    
    
    
date_test = in_date()


    

julian_weekday(julian_day(date_test))
        
        
        
         
        
        
        
    


