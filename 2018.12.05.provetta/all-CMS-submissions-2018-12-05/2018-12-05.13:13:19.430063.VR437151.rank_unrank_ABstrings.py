"""
* user:  VR437151
* fname: GIACOMO
* lname: BARTOLI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 13:13:19.430063
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    if input_string[i] == 'A':
        return 0
    else:
        return 1
            

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

