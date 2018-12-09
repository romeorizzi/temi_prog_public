"""
* user:  VR429690
* fname: ALBERTO
* lname: AMBROSI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:05:14.812614
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def conta_multipli(a, b, c):
    out=0
    for i in range(c):
        if i%a==0 and not i%b==0:
            out=out+1
    return out
    
a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))


    
