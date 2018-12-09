"""
* user:  VR437112
* fname: ALESSANDRO
* lname: SIGNORETTO
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 12:13:46.481852
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
    while (i<len(p)):
       if (p[i]>p[i+1]):
          n=n+1
       i=i+1
    return n

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
