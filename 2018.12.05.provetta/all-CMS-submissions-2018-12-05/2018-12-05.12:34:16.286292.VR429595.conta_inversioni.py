"""
* user:  VR429595
* fname: GAIA
* lname: VIVIAN
* task:  conta_inversioni
* score: 60.0
* date:  2018-12-05 12:34:16.286292
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p): 
    n=0
    for i in range (len(p)-1):
        for j in range (i,len(p)):
            if (p[i]>p[j]):
                n=n+1
                t=p[i]
                p[i]=p[i+1]
                p[i+1]=t
    return n

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
