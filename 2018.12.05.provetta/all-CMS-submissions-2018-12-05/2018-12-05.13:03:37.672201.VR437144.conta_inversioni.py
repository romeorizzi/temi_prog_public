"""
* user:  VR437144
* fname: SIMONE
* lname: SORGATO
* task:  conta_inversioni
* score: 15.0
* date:  2018-12-05 13:03:37.672201
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    n=int(0)
    i=int(0)
    j=int(i+1)
    t=len(p)
    while (j<t):
        if (p[i]>p[j]):
           i=i+1
           j=i+1
           n=n+1
        else:
           i=i+1
           j=j+1          
    return n
p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
