"""
* user:  VR429591
* fname: SARA
* lname: AVESANI
* task:  conta_multipli
* score: 20.0
* date:  2018-12-05 12:10:10.554875
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    count=0
    for i in range(len(p)):
        x=p[i]
        for j in range(i,len(p)):
            if x>p[j]:
                count= count+1
    return count

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
