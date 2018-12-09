"""
* user:  VR429670
* fname: ENRICO
* lname: NEGRO
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:17:55.694140
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    c=len(p)
    x=0
    n=1
    for i in range(c):
        for j in range(n,c):
            if p[i]>p[j]:
                x=x+1
        n=n+1

    return x
    

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
