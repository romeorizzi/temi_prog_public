"""
* user:  VR429625
* fname: GIOVANNI
* lname: LORENZI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 12:55:14.597564
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    n=0
    for i in range (0, len(s),):
        print (i)
        if s[len(s)-1-i]=='A':
            m=0
        else:
            m=1
        n=n+m*2**(i)
    return(n)


        

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

