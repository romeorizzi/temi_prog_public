"""
* user:  LucaFaccioli
* fname: LUCA
* lname: FACCIOLI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 13:20:27.937348
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):    
    inv=0
    for i in range(0, len(p)):
        for j in range(i+1, len(p)):
            if(p[i]>p[j]):
                inv+=1
    return inv

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
