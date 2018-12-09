"""
* user:  VR437156
* fname: VALERIO
* lname: FLORA
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 12:32:16.453440
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    l=0
for i in range (len(p)):
    for j in range((i+1), len(p)):
        if(p[i]>p[j]):
            l=l+1
    return l
    

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
