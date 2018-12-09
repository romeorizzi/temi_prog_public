"""
* user:  VR437468
* fname: MATTEO
* lname: D'ALESSANDRO
* task:  conta_inversioni
* score: 60.0
* date:  2018-12-05 12:08:21.336580
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    invtot=0
    invparz=1
    aus=0
    while (invparz>0):
        invparz=0
        for i in range(0,len(p)-1):
            if (p[i]>p[i+1]):
                invparz=invparz+1
                invtot=invtot+1
                aus=p[i]
                p[i]=p[i+1]
                p[i+1]=p[i]
    return invtot

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
