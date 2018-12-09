"""
* user:  VR429663
* fname: DENNIS
* lname: MODESTI
* task:  rank_unrank_ABstrings
* score: 100.0
* date:  2018-12-05 12:21:06.859097
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def map_char_to_num(c):
    if c == "A":
        return 0
    else:
        return 1
    

def map_num_to_char(n):
    return ["A","B"][n]

def ABstring2rank(s):
    e = len(s)-1
    n = 0
    for i in s:
        n += map_char_to_num(i) * 2**(e)
        e-=1
    return n

def ABstring_of_len_and_rank(length, r):
    s = ""     
    while r>0:
        s+=map_num_to_char(r%2)
        r//=2
    while len(s) < length:
        s+=map_num_to_char(0)
    return s[::-1]

input_string = raw_input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

