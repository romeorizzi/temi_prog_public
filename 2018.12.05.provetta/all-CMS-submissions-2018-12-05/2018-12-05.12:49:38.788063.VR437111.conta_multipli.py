"""
* user:  VR437111
* fname: LUCA
* lname: CHIAVEGATO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:49:38.788063
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def conta_multipli(a, b, c):
    i=0
    for z in range(1,c+1):
       
       if z%a==0 and z%b!=0:
          i=i+1
    return i
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
