"""
* user:  VR437206
* fname: FEDERICA
* lname: BIANCO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 13:04:54.661119
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
    
def conta_multipli(a,b,c):
    n=int(c/a)
    p=1
    while (n*a==c):
        if (n*ab==0):
            n=n+1
            p=p+1
    return (n)

    
a, b, c = map(int, raw_input().strip().split())
print(conta_multipli(a, b, c))
