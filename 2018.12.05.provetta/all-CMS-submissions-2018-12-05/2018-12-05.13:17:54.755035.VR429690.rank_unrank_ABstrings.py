"""
* user:  VR429690
* fname: ALBERTO
* lname: AMBROSI
* task:  rank_unrank_ABstrings
* score: 100.0
* date:  2018-12-05 13:17:54.755035
"""
from __future__ import division, print_function

def binariodec(a):  #da stringa
    x=0
    for i in range (len(a)):
        x=x+(int(a[i])*(2**(len(a)-(1+i))))
    return x


def stringtobin(stringa):
    c=""
    for i in range(len(stringa)):
        if stringa[i]=="A":
            c=c+str(0)
        else:
            c=c+str(1)
    return c

def dectobin(a):
    ris=""
    c=""
    while a!=0:
        ris=ris+str(a%2)
        a=a//2
    for i in range(len(ris)-1,-1,-1):
        c=c+ris[i]
    return c

def bintostring(n):
    ris=""
    for i in range(len(n)):
        if n[i]=="0":
            ris=ris+"A"
        else:
            ris=ris+"B"
    return ris

def stringab(n,a):
    c=""
    for i in range(n-len(a)):
        c=c+"A"
    c=c+a
    return c
    

 #!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s): 
    return binariodec(stringtobin(s))

def ABstring_of_len_and_rank(length, r):
    
    return stringab(length,bintostring(dectobin(r)))  


input_string = raw_input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )


