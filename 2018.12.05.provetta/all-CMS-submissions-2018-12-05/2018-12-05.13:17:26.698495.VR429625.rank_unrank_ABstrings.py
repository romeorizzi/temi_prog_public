"""
* user:  VR429625
* fname: GIOVANNI
* lname: LORENZI
* task:  rank_unrank_ABstrings
* score: 50.0
* date:  2018-12-05 13:17:26.698495
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def ABstring2rank(s):
    n=0
    for i in range (0, len(s)):
        if s[len(s)-1-i]=='A':
            m=0
        else:
            m=1
        n=n+m*2**(i)
    return(n)


def ABstring_of_len_and_rank(length, r):
    s=''
    k=1
    a=('A')
    b=('B')
    while r>0:
        if r%2==0:
            s=s+a
        elif r%2==1:
            s+=b
        r//=2
    return s    


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )
