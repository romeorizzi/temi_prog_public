"""
* user:  VR437373
* fname: MARCO
* lname: QUANILLI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 13:03:31.190966
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    somma=0
    i=len(s)-1
    while(i>=0):
        if(s[i]=="B"):
            somma=somma+2**i 
        i=i-1                      
    return somma

def ABstring_of_len_and_rank(length, r):
    stringa=""
    while(length>0):
        if(r>0):
            if(2**(length-1)<=r):
                stringa="B"+stringa
                r=r-2**(length-1)
            else:
                stringa="A"+stringa
            length=length-1
        else:
            length=0
    return stringa        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

