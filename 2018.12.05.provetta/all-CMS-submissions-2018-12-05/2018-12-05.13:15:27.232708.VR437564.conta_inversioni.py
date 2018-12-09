"""
* user:  VR437564
* fname: GIORDANO
* lname: CORBIOLI
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:15:27.232708
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    n=0
    for i in range (len(p)):
        for j in range (i+1, len(p)):
            if (p(i)<p(j)):
                n=n+1
    return n

p = list(map(int,raw_input().strip().split()))
print(numero_di_inversioni(p))
