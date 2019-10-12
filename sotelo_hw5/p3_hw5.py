#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Asis A Sotelo
#Time Server
#p3_hw5
#23Jul19 Created Program 
#




import time 


USAGE="""
usage: p3_hw5.py 

       Serves data for a TCP port 55555
"""


import sys
import os
import socket

###############################################################################


print("Program Launched Attempting to Setup Server:")

###############################################################################


###############################################################################



def bind_port(prt):
   """Create socket and bind to port prt.
   """

   host = ''  # bind to all available interfaces
 
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse port
   s.bind((host, prt))
   s.listen(1)
    
   return(s)
###############################################################################

thesocket = bind_port(55555) 

outdata = b'\n\n Hello from the port 55555\n\n'



while True:
    
     
    print("Server at  Port 55555 Created") 
    connection, peer = thesocket.accept()
    x = "Connection established at : " + time.ctime()
    time_connect = bytes(x,'utf-8')
    connection.sendall(time_connect)	
    time.sleep(2) 
    print('Sending data to %s...' % repr(peer), end='')
    
    connection.sendall(outdata) 
    print('Done.\n')
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()

