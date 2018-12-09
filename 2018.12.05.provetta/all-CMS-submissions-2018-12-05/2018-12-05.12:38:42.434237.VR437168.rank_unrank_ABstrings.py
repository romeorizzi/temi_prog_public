"""
* user:  VR437168
* fname: GIACOMO
* lname: SCHIESARI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 12:38:42.434237
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    i = 0
    somma = 0
    while i < len(s):
        if s[i] == 'A':
            somma = somma + 0
        else:
            somma = somma + 2^(i)
        i = i + 1
    return somma

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

