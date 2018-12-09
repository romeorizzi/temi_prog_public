"""
* user:  VR429709
* fname: DAVIDE
* lname: FORNARI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 11:45:55.394324
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    n=0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if(p[j]<p[i]):
                n+=1
    return n
    

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
