"""
* user:  VR429663
* fname: DENNIS
* lname: MODESTI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:46:50.157304
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    counter = 0
    for (n,i) in enumerate(p):
        for j in p[n+1:]:
            if i>j:
                counter+=1
    return counter
        

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
