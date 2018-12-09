"""
* user:  VR437012
* fname: Giosue
* lname: Cavagna
* task:  rank_unrank_ABstrings
* score: 50.0
* date:  2018-12-05 13:15:00.234366
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def divide (n, d):
    if n%d == 0:
        return True
    return False

def ABstring2rank(s):
    res=0
    trad=0
    i=0
    while i<len(s):
        if s[i]=='A':
           trad=0
        if s[i]=='B':
           trad=2**((len(s)-1)-i)

        res=res+trad
        i=i+1
   
    return res
    

def ABstring_of_len_and_rank(length, r):
    res=[]
    c=0
    for i in range(0,length):
        res[0:0]='A'
    if divide(r,2)==False:
        res[length-1]='B'
    r=r-1
    while divide(r,2):
        r=r/2
        c=c+1
    res[(len(res)-1)-c]='B'
    return res

input_string = raw_input()

if input_string[0] == 'A' or input_string[0] == 'B': 
 print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

