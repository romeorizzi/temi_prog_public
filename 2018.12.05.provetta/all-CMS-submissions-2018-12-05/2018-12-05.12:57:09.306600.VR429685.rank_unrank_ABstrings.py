"""
* user:  VR429685
* fname: SOFIA
* lname: RIZZOTTO
* task:  rank_unrank_ABstrings
* score: 100.0
* date:  2018-12-05 12:57:09.306600
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings

def esponente(x,a):
    n=1
    o=1
    while n<a:
        o=o*x
        n += 1
    return (o)

def ABstring2rank(s):
    sol=0
    for i in range(len(s)):
        if s[i]=='B':
            sol=sol+esponente(2,len(s)-i)
    return (sol)

def ABstring_of_len_and_rank(length, r):
    m=''
    for i in range(length):
        if r%2==0:
            m=m+'A'
        else:
            m=m+'B'
        r=r//2
    return (m[::-1])


input_string = raw_input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print ( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print ( ABstring_of_len_and_rank(int(length), int(r)) )

