"""
* user:  VR429620
* fname: LETIZIA
* lname: PACCINI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 12:51:23.322719
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    a="A"*len(s)
    print(a)
    conta=0
    while(a!=s):
        i=len(a)-1
        while(i>=0 and a!=s):
            if(i==len(a)-1):
                a=a[0:len(a)-1]+"B"
                print(a)
            else:
                salva1=a[i]
                salva2=a[i+1]
                a=a[0:i]+salva2+salva1+a[i+2:len(a)]
                print(a)
            i=i-1
            conta+=1
    return conta      

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )

