"""
* user:  VR437468
* fname: MATTEO
* lname: D'ALESSANDRO
* task:  rank_unrank_ABstrings
* score: 100.0
* date:  2018-12-05 12:13:22.133343
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    pos=1
    ran=0
    for i in range(len(s)-1,-1,-1):
        if (s[i]!='A'):
            ran=ran+pos
        pos=pos*2
    return ran

def ABstring_of_len_and_rank(length, r):
    s=''
    for i in range(length-1,-1,-1):
        if(r%2==1):
            s='B'+s
        else:
            s='A'+s
        r=int(r/2)
    return s
       


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

