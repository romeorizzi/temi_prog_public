"""
* user:  VR429626
* fname: ARIANNA
* lname: PELLIZZARO
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 13:18:12.151806
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    l=len(s)
    x=0
    for i in range (0, l, 1):
        if s[i]=='B':
            for 
            x=x+2^(l-1-i)
    return x
        
            
                
        

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

