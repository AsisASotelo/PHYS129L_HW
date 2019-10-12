#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Asis A Sotelo

#hw5_p1.py
#Get Web Page


#22Jul19 Created Program
#23jul19 Changed the String Method of Parsing to BS4
USAGE="""
usage: 

       Connects to UCSB Lipman Website and Gets HTML parses to get Last Update
"""
N_ARGUMENTS = (1,2)

from  bs4 import BeautifulSoup
import sys
import os
import socket
import re
################################################################
###############################################################################

###############################################################################

def open_connection(ipn, prt):
   """Open TCP connection to ipnum:port.
   """
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
   connect_error = s.connect_ex((ipn, prt))

   if connect_error:
      if connect_error == 111:
         usage('Connection refused.  Check address and try again.')
      else:
         usage('Error %d connecting to %s:%d' % (connect_error,ipn,prt))

   return(s)
###############################################################################

def receive_data(thesock, nbytes):
   """Attempt to receive nbytes of data from open socket thesock.
   """
   dstring = b''
   rcount = 0  # number of bytes received
   thesock.settimeout(5)
   while rcount < nbytes:
      try:
         somebytes = thesock.recv(min(nbytes - rcount, 2048))
      except socket.timeout:
         print('Connection timed out.', file = sys.stderr)
         break
      if somebytes == b'':
         print('Connection closed.', file = sys.stderr)
         break
      rcount = rcount + len(somebytes)
      dstring = dstring + somebytes
      
   print('\n%d bytes received.\n' % rcount)
   return(dstring)  
###############################################################################



print()
print('Connecting to %s, port %d...\n' % ('http://web.physics.ucsb.edu', 80))

thesocket = open_connection('web.physics.ucsb.edu', 80)
 

### REQUEST LINE
  
thesocket.sendall(b'GET /~phys129/lipman/ HTTP/1.0\r\n\r\n')
   
indata = receive_data(thesocket, 4096)
thesocket.shutdown(socket.SHUT_RDWR)
thesocket.close()

## The following parses the data with BS4

soup = BeautifulSoup(indata,"html.parser")

text = soup.p.span.string


print("Last Update: " + text)


