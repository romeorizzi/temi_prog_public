"""
* user:  VR429705
* fname: MATTIA
* lname: BOMBIERI
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:09:37.585871
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    inversioni = 0
    for i in range(0, len(p)):
        for j in range(i+1, len(p)):
            if (p[i], p[j]):
                inversioni = inversioni + 1
    return inversioni

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
