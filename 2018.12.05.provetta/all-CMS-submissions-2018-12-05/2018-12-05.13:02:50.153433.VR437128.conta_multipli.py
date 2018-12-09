"""
* user:  VR437128
* fname: SOFIA
* lname: SCHIO
* task:  conta_multipli
* score: 80.0
* date:  2018-12-05 13:02:50.153433
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
    
def conta_multipli(a, b, c):
    n=int(c/a)
    i=1
    while i*a*b<=c :
        n=n-1
        i=i+1
    return n
    
a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))
