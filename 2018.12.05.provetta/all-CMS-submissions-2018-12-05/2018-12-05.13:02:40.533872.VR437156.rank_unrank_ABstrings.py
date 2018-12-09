"""
* user:  VR437156
* fname: VALERIO
* lname: FLORA
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 13:02:40.533872
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    ABstring2rank.sort(reverse=True)
    return(s)
    
        
    return 42

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

