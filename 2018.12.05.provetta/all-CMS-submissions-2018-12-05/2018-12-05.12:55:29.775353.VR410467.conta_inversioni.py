"""
* user:  VR410467
* fname: LUCA
* lname: DE TOGNI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:55:29.775353
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    d = 0
    for i in range(len(p)):
        a = 0
        b = 1
        while (a<(len(p)-1)) and (b<len(p)):
            if p[a]>p[b]:
                d=d+1 
                c = p[a]
                p[a] = p[b]
                p[b] = c
            a = a+1
            b = b+1
           
    return d

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
