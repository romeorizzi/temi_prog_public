"""
* user:  LucaFaccioli
* fname: LUCA
* lname: FACCIOLI
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:14:13.370046
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):    
    n=0
    for i in range(1, len(p)-1):
        if p[0]>p[1]:
            n+=1  
    return n

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
