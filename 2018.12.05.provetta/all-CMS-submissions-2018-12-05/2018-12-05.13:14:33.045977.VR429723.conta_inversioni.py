"""
* user:  VR429723
* fname: VERONICA
* lname: GUIDOLIN
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:14:33.045977
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

p = list(map(int, input().strip().split()))
def numero_di_inversioni(p):
    for i in range(0,len(p)):
        for j in range(i,len(p)):
        p[i]>p[j]

print(numero_di_inversioni(p))
