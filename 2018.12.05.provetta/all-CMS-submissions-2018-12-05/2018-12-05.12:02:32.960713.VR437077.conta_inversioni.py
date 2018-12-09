"""
* user:  VR437077
* fname: FABIO
* lname: MARINI
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 12:02:32.960713
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    conta = 0
    k = 0
    i = 0
    j = 0
    while i<(len(p)-2):
        for j in range(i+1, len(p)):
            if (p[i] > p[j]):
                conta += 1
            k = k+1
        i += 1
    return conta

p = list(map(int, raw_input().strip().split()))
print(numero_di_inversioni(p))




