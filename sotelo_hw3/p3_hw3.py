#!/usr/bin/env python3

#Problem 3 Homework 3
#Asis A Sotelo
#11Jul2018
#Works only With PYTHON3
#p3_hw3.py

""" STRING PROCESSING """

""" A. PROMPTS THE USER FOR A STRING WITH AT LEAST 3 WORDS"""


flag = True ## Creates a boolean value for the while loop


while flag: ##WHILE LOOP THAT CHECKS BOOLEAN VALUE OF "flag"

    instr = input("Please enter a string with 3 words:\n ")
    split_user_in_1 = instr.split()##Splits the string with ' ' delimiter.



##B. Rejects strings with < 3 words


    if (len(split_user_in_1) != 3):##Uses the value of conditional that checks for 3
        print("Input did not contain 3 words.")
        ##'flag' True so the loop continues
    else:
        break ## The break exits the loop once it has checked for size

""" C. Prints the words in the string, one per line"""
type(split_user_in_1)

for i in range(len(split_user_in_1)):
    print(split_user_in_1[i])


""" D. Prints first 3 characters of string """

print(instr[:3])

""" E. Prints last 3 characters of string """

print(instr[-5:])

"""Prints the last half of the string (include any characters on the boundary)"""

print(instr[-int((len(instr))/2):])


""" H. Prints the string with the words in reverse order"""

print(instr[::-1])

"""i. Prints the string with the words alphabetized"""

print(instr.upper())

"""j. Prints each character in the string, one per line"""

for i in range(len(instr)):

    print(instr[i])


"""k. Prints hexadecimal values for each character in the string, one line per character"""

for i in range(len(instr)):

    print(hex(ord(instr[i])))

