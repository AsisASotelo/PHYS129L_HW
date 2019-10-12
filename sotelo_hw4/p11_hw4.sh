#!/bin/bash
# -*- coding: utf-8 -*-

#Asis A Sotelo
#p11_hw4.py
#WGET,GREP,and SED

#18Jul2019


wget -qO- http://web.physics.ucsb.edu/~phys129/lipman/ | # Gets Website with options quiet and O not outputting to file just STDOUT
grep -i  Latest | # Finds Line with GREP and the Keyword LATEST
# SED uses option -e which then runs the following script which is s/../ 
#which is a substition script with the ^.* being the wild that matches "> and
#deletes it by replacing it with nothing. The second substituion replaces the 
#other part of html file and the last one puts a space where the "&nbsp" is 
sed -e 's/^.*">//' -e 's/<.*$//' -e 's/&nbsp;/ /g' 