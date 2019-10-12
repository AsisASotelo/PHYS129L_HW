#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#p8_hw4.py
#POSTSCRIPT FLOWER
#18Jul2019


flag = True

while flag:
    
    num_pet = int(input("Enter Number of Petals"))
    
    if 0<num_pet< 6:
        break

angle = (360/num_pet)
width = (1/num_pet)


listofstrings =[]
listofstrings2 = []
for i in range(num_pet):
    
    listofstrings.append(str(angle*i))
    listofstrings2.append(str(width))
    
print(listofstrings)
    

first_part = """
%!PS
%
% petal.ps - Draw flower petal
%
% 05May16  Everett Lipman
%

%
% draw petal scaled by xscale and yscale, rotated by angle.
%
/petal  % xscale yscale angle petal
   {
   /petalcol [ 0.8 0 0 ] def
   /ep1 [ 0 0 ] def
   /ep2 [ 0 100 ] def
   /cp1 [ 55 65 ] def
   /cp2 [ 10 95 ] def
   /ap {aload pop} def
   gsave
   petalcol ap setrgbcolor
   0 setlinewidth
   rotate  % use angle from stack
   scale   % use xscale and yscale from stack

   ep1 ap moveto
   cp1 ap cp2 ap ep2 ap curveto
   cp2 ap exch neg exch
   cp1 ap exch neg exch
   ep1 ap curveto closepath fill
   
   grestore
   } def

gsave
   306 500 translate

"""
   #1 1 0 petal
   #1 1 90 petal
   #0.4 1 195 petal
  # 1 2 255 petal

   
   
last_part = """grestore

showpage

"""

for i in range(num_pet):
    
    first_part += "   " + listofstrings2[i] + " 1 " + listofstrings[i] + " petal\n"
    

full = first_part + last_part

print(full)

file = open("petals.ps", "w")
file.write(full)
file.close()
