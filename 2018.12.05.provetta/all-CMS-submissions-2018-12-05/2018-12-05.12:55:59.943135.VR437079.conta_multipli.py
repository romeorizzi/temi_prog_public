"""
* user:  VR437079
* fname: GIULIA
* lname: ALTOBEL
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:55:59.943135
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
   n=0
   for i in range (len(p):
     for j in range (i+1, len (p):
       if (p(i)<p (j)):
            n=n+1
return n 
p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
