"""
* user:  VR429690
* fname: ALBERTO
* lname: AMBROSI
* task:  conta_inversioni
* score: 60.0
* date:  2018-12-05 11:51:26.277718
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    c=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]:
                save=p[i]
                p[i]=p[j]
                p[j]=save
                c=c+1
    return c

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
