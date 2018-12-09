"""
* user:  VR437653
* fname: LUCA
* lname: PESERICO
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:52:45.910668
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa è la funzione che devi perfezionare
    somma=n1+n2
    if n1==n2:
        return (0,0)
    elif n1>n2:
        if (n1+n2)%2==0:
            return (2,0)        
        else:
            return (1,0)
    elif n2>n1:
        if (n2+n1)%2==0:
            return (0,2)
        else:
            return (0,1)        
    
            
     
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)
