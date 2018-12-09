"""
* user:  VR429669
* fname: DAVIDE
* lname: CAMPONOGARA
* task:  rank_unrank_ABstrings
* score: 100.0
* date:  2018-12-05 12:59:08.768591
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input


# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    soluzione=0
    for i in range(0,len(s)):
        if(s[len(s)-1-i]=="B"):
            soluzione+=2**i
    return soluzione

def ABstring_of_len_and_rank(length, r):
    parola=""  
    while(r!=0):
        if(r%2==0):
            parola="A"+parola
        else:
            parola="B"+parola
        r=int(r/2)
    if(len(parola)<length):
        parola="A"*(length-len(parola))+parola
    return parola   

input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )


