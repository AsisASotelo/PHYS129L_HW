#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#Get Web Page With Request
#p2_hw5

#23Jul2019

from bs4 import BeautifulSoup 
import numpy as np 
import requests 
import re
import pdb; pdb.set_trace()
r= requests.get("http://web.physics.ucsb.edu/~phys129/lipman/")

soup = BeautifulSoup(r.text ,'html.parser')
date = soup.p.span.string


print("Last Update: %s" % date)



