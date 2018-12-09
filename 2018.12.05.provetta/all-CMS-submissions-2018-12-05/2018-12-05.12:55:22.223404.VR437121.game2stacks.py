"""
* user:  VR437121
* fname: PIETRO
* lname: GIOVANNONI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:55:22.223404
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

def play(n1, n2):  
    if n1==n2:
        return (0,0)
    elif n1>n2:
        return (n1-n2, 0)
    elif n1<n2:
        return (0, n2-n1)
if n1>=0 and n2>=0:
    togli1, togli2 = play(n1, n2)
    print(togli1)
    print(togli2)
else:
    print("valori non accettabili")
