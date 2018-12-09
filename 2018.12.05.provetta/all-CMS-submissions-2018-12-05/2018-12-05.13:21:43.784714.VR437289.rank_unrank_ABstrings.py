"""
* user:  VR437289
* fname: ALVIANO
* lname: MASENELLI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 13:21:43.784714
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    x=0
    for i in range (0,len(s)):
        if (s[i]=='B'):
                x=x+2**(len(s)-1-i)
    return x

     




def ABstring_of_len_and_rank(length, r):
    risultato = ''
    for i in range (length-1,-1,-1):
        x=(2**i)
        if(r>=x):
            risultato+='B'
            r=r-x
        else:
            risultato+='A'
    return risultato

input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

