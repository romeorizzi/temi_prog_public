"""
* user:  VR437269
* fname: MATTEO
* lname: BONINI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 12:15:36.446475
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    x = 0
    n = len(s)
    for i in range(n):
        if s[i] == 'B':
            x = x + 2**(n-i-1)
    return x

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

