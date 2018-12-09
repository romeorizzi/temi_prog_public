"""
* user:  VR429690
* fname: ALBERTO
* lname: AMBROSI
* task:  rank_unrank_ABstrings
* score: 0.0
* date:  2018-12-05 12:58:28.764959
"""
def binariodec(a):
    r=str(a)
    x=0
    for i in range (len(r)):
        x=x+(int(r[i])*(2**(len(r)-(1+i))))
    return x


def stringtobin(stringa):
    c=""
    for i in range(len(stringa)):
        if stringa[i]=="A":
            c=c+str(0)
        else:
            c=c+str(1)
    return c

def dectobin(a):
    ris=""
    c=""
    while a!=0:
        ris=ris+str(a%2)
        a=a//2
    for i in range(len(ris)-1,-1,-1):
        c=c+ris[i]
    return int(c)


 #!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s): 
    return binariodec(stringtobin(s))

def ABstring_of_len_and_rank(length, r):
    return "ABBA"        


input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )


