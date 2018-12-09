"""
* user:  VR437121
* fname: PIETRO
* lname: GIOVANNONI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:55:13.365295
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input



def numero_di_inversioni(p):
    n=0
    l=len(p)
    for i in range(0, l):
        for j in range(0, l):
            if p[i]>p[j] and i<j:
                n=n+1
    return n


p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
