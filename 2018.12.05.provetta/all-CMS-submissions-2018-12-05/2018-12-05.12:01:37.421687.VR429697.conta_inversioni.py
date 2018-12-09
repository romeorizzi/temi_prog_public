"""
* user:  VR429697
* fname: GABRIELE
* lname: BALDO
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:01:37.421687
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input



def numero_di_inversioni(p):   
    m=0    
    for i in range(0, len(p)):
        for t in range((i), len(p)):
            if p[i]>p[t]:
                m=m+1
    return m           








p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
