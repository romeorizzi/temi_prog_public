"""
* user:  VR437210
* fname: JACOPO
* lname: QUIRINALI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:52:59.301915
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    k=len(p)
    k=k-1  
    cont=0
    while(k>=0):    
        i=k
        j=k+1
        while(j<len(p) and p[i]>p[j]):
            a=p[i]
            b=p[j]
            if(a>b):                
                p[j]=a
                p[i]=b
                cont=cont+1
            i=i+1
            j=j+1  
        k=k-1
    return cont

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
