"""
* user:  VR429620
* fname: LETIZIA
* lname: PACCINI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:04:55.608058
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
    
def conta_multipli(a, b, c):
    n=0
    i=1
    while(a*i<=c):
        if not((a*i)%b==0):
            n+=1
        i+=1
    return n
    
a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))
