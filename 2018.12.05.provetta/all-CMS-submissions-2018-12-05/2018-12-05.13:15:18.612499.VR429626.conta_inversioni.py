"""
* user:  VR429626
* fname: ARIANNA
* lname: PELLIZZARO
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 13:15:18.612499
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    x=0
    for i in range (len(p)):
        for j in range (i, len(p), 1):
            if p[i]>p[j]:
                x+=1
    return x

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
