"""
* user:  VR437151
* fname: GIACOMO
* lname: BARTOLI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 13:10:25.242432
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
    
def conta_multipli(a, b, c):
    n = 0   
    for i in range (c+1):
        if i%a == 0:
            n = n+1
        if i%b == 0 and i%a == 0:
            n = n-1     
    return(n)

a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))
