"""
* user:  VR437012
* fname: Giosue
* lname: Cavagna
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 13:12:55.845934
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    c=0
    res=0
    i=1
    while c<len(p):     
        while i<(len(p)-c):
          if p[c]>p[c+i]:
              res=res+1
          i=i+1
        i=0
        c=c+1
    return res

p = list(map(int, raw_input().strip().split()))
print(numero_di_inversioni(p))
