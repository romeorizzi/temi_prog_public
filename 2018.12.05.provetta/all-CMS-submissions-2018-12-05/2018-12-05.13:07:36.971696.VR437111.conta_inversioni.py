"""
* user:  VR437111
* fname: LUCA
* lname: CHIAVEGATO
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:07:36.971696
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    c=0
    for i in range (len(p)):
       x=p[i]
       for j in range(i,n(p)):
          if x>p[j]:
            c=c+1
    return c
           

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
