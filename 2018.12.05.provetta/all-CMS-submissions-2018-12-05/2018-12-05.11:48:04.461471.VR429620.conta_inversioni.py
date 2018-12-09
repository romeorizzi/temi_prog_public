"""
* user:  VR429620
* fname: LETIZIA
* lname: PACCINI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 11:48:04.461471
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    
    inversioni=0
    for x in range (len(p)):
        i=0
        while(i<len(p)-1):
            if(p[i]>p[i+1]):
                inversioni+=1
                salva=p[i]
                p[i]=p[i+1]
                p[i+1]=salva
            i+=1
    return inversioni

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
