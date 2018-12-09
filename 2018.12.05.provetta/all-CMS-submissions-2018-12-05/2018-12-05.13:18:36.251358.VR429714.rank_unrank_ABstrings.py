"""
* user:  VR429714
* fname: DOMENICO
* lname: DI GRAZIA
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 13:18:36.251358
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    k=0
    for i in range (0, len(s)):
        if s[i]=='B':
           k=k+2**(len(s)-1-i)       
    return k

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

