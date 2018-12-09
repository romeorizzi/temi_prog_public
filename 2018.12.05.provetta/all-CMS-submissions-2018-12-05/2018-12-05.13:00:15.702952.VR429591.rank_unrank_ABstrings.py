"""
* user:  VR429591
* fname: SARA
* lname: AVESANI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 13:00:15.702952
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    posizione= 0
    length_list_ord= 2**(len(s))
    for i in range(len(input_string)):
        if input_string[i]=='A':
            posizione=posizione
        elif input_string[i]=='B':
            posizione= length_list_ord-1
        else: 
            if input_string[i]
        
         
        
        
        return posizione

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        




input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

