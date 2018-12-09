"""
* user:  AnnachiaraForino
* fname: ANNACHIARA
* lname: FORINO
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:18:16.463587
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
   input = raw_input # in python2, l'equivalente di input è raw_input


p = list(map(int, input().strip().split()))

def numero_di_inversioni(p):  
    inversioni=0
    for i in range(0, len(p)):
        for i in range(i+1, len(p)):
             if p[i]>p[j]:
                   inversioni += 1
        
            

    return inversioni
    
    
    
    


print(numero_di_inversioni(p))
