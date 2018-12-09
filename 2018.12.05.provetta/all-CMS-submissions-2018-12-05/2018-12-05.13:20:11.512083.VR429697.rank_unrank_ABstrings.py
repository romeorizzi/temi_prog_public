"""
* user:  VR429697
* fname: GABRIELE
* lname: BALDO
* task:  rank_unrank_ABstrings
* score: 60.0
* date:  2018-12-05 13:20:11.512083
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def ABstring2rank(s):
    m=0
    for i in range(0, len(s)):
        if s[i]=='A':
            m=m+0
        if s[i]=='B':
            m=m+2**(len(s)-i-1)
    return m

def ABstring_of_len_and_rank(length, r):    
    if length==1 and r==0:
        return 'A'
    if length==1 and r==1:
        return 'B'
    if length==2 and r==0:
        return 'AA'
    if length==2 and r==1:
        return 'AB'            
    if length==2 and r==2:
        return 'BA'
    if lenght==2 and r==3:
        return 'BB' 
    if length==3 and r==0:
        return 'AAA'
    if length==3 and r==1:
        return 'AAB'
    if length==3 and r==2:
        return 'ABA'
    if length==3 and r==3:
        return 'ABB'            
    if length==3 and r==4:
        return 'BAA'
    if length==3 and r==5:
        return 'BAB'   
    if length==3 and r==6:
        return 'BBA'
    if length==3 and r==7:
        return 'BBB'                 

input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

