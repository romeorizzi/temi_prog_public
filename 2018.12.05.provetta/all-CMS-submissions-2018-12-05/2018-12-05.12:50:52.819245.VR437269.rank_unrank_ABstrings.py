"""
* user:  VR437269
* fname: MATTEO
* lname: BONINI
* task:  rank_unrank_ABstrings
* score: 80.0
* date:  2018-12-05 12:50:52.819245
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    x = 0
    n = len(s)
    for i in range(n):
        if s[i] == 'B':
            x = x + 2**(n-i-1)
    return x

def ABstring_of_len_and_rank(length, r):
    p = []
    for i in range(length):
        p.append('A')

    while r!=0 :
        for i in range(length):
            if (2**i <= r) & (r <= 2**(i+1)):
                p[length-i-1] = 'B'
                r = r-2**i
    s = ''
    for i in range(length):
        if p[i]=='A':
            s = s + 'A'
        else:
            s = s + 'B'
    return s        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

