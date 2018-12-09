"""
* user:  VR437011
* fname: SARA
* lname: QUINTO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:49:08.126365
"""


# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
    
def conta_multipli(a, b, c):
    k = 0
    for n in range (1, c+1):
        if n%a == 0 and n%b != 0:
            k = k+1 
    return k  

a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))
