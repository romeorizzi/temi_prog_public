"""
* user:  VR429709
* fname: DAVIDE
* lname: FORNARI
* task:  rank_unrank_ABstrings
* score: 100.0
* date:  2018-12-05 12:07:45.680953
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    rk=0
    for i in range(len(s)):
        rk=rk+(2**(len(s)-1-i))*(ord(s[i])-ord('A'))
    return rk

def ABstring_of_len_and_rank(length, r):
    t=""
    for i in range(length):
        if(r%2==0):
            r=r/2
            t="A"+t
        else:
            r=(r-1)/2
            t="B"+t
    return t        


input_string = raw_input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

