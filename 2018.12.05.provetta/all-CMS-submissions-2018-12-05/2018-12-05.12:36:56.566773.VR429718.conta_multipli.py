"""
* user:  VR429718
* fname: GIADA
* lname: SOSO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:36:56.566773
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
    
def conta_multipli(a, b, c):
    z=0
    for i in range (1,c+1)
        if i%a==0:
            if b%0!=0:
                z=z+1
    return z
            
    
a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))
