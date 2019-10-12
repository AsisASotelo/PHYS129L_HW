#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Asis A Sotelo
#Dictionaries and Databases
#11Jul2019

import numpy as np

data_file = "dictionary.csv"
data_set = np.genfromtxt(data_file,dtype='str',delimiter=',')


list_of_data = []
for i in range(len(data_set)):
    list_of_data.append({'Last':data_set[i][0],'First':data_set[i][1],'Color':data_set[i][2],'Food':data_set[i][3]})
    
    



def print_keys():
    i=0
    print("_________________________\n")
    print("THE KEYS OF DICTIONARY:\n")
    for key in sorted(list_of_data[0].keys()):
        i=i+1
        print(i,key)
        
    print("0 KEY TO EXIT PROGRAM")
    
    
    
    
    

 
    
    



flag = True

while flag:
    
    
    print_keys()
    print()
    choice = int(input(">>CHOOSE KEY NUMBER<<:\n"))
        
    if choice == 1:
        
        string1=[]
        for k in range(len(list_of_data)):
            
            string1.append(list_of_data[k].get('Last') + ", " + list_of_data[k].get('First') + ":  " + list_of_data[k].get('Color'))
          
       
        string1.sort()
        
        for l in range(len(string1)):
            print(string1[l])
        
            
    elif choice == 2:
        string2=[]
        for k in range(len(list_of_data)):
            
            string2.append(list_of_data[k].get('Last') + ", " + list_of_data[k].get('First') + ":  " + list_of_data[k].get('First'))
          
       
        string2.sort()
        
        for l in range(len(string2)):
            print(string2[l])          
            
    elif choice == 3:
        string3=[]
        for k in range(len(list_of_data)):
            
            string3.append(list_of_data[k].get('Last') + ", " + list_of_data[k].get('First') + ":  " + list_of_data[k].get('Food'))
          
       
        string3.sort()
        
        for l in range(len(string3)):
            print(string3[l])
            
        
            
    elif choice == 4:
        string4=[]
        for k in range(len(list_of_data)):
            
            string4.append(list_of_data[k].get('Last') + ", " + list_of_data[k].get('First') + ":  " + list_of_data[k].get('Last'))
          
       
        string1.sort()
        
        for l in range(len(string4)):
            print(string4[l])
        
    elif choice == 0:
        break
    
    
                               
        
        
        
    
      