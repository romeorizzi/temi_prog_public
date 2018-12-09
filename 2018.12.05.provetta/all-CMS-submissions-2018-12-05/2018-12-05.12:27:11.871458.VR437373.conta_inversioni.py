"""
* user:  VR437373
* fname: MARCO
* lname: QUANILLI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:27:11.871458
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    i=1
    m=0
    s=len(p)
    while(s!=0):
        i=1
        s=len(p)-1
        while(i<len(p)):        
            if(p[i-1]>p[i]):
                l=p[i-1]
                p[i-1]=p[i]
                p[i]=l
                m=m+1
            else:
                s=s-1
            i=i+1
    return m

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
