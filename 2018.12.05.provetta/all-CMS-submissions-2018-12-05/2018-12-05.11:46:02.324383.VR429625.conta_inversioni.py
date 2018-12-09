"""
* user:  VR429625
* fname: GIOVANNI
* lname: LORENZI
* task:  conta_inversioni
* score: 45.0
* date:  2018-12-05 11:46:02.324383
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    inversioni=0
    for i in range(0,len(p)-1):
        while p[i]>p[i+1]:
            for x in range (0,len(p)-1):
                h=p[x]
                k=p[x+1]
                if h>k:
                    p[x]=k
                    p[x+1]=h
                    inversioni+=1
    return inversioni

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
