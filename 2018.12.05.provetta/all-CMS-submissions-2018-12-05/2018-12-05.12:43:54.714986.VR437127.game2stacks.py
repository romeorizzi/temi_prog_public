"""
* user:  VR437127
* fname: GIOVANNI
* lname: FOSCARIN
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:43:54.714986
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione per il problema rank_unrank_ABstrings
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input


# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa è la funzione che devi perfezionare

    if n1==n2:
        return (0,0)
    if n1<n2:
        return (0,n2-n1)


    if n1>n2:
        return (0,n1-n2)
       

    
                 # non arrenderti sempre!
   
   


togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

