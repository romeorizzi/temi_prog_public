"""
* user:  VR429667
* fname: FEDERICO
* lname: ZANCAN
* task:  conta_inversioni
* score: 60.0
* date:  2018-12-05 12:36:48.944367
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    l = len(p)    
    s = 0
    k = 0
    i = 0
    while i < l:
        for j in range (i+1,l):
            if p[i] > p[j]:
                s = p[i]
                p[i] = p[j]
                p[j] = s
                k += 1
        i += 1

    return k

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
