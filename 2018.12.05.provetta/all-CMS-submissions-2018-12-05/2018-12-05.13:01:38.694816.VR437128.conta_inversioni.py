"""
* user:  VR437128
* fname: SOFIA
* lname: SCHIO
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 13:01:38.694816
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    i=0
    n=0
    while i<len(p) :
        j=i
        while j<len(p) :
            if p[i]>p[j] :
                n=n+1
            j=j+1
        i=i+1
    return n
p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
