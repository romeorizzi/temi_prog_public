"""
* user:  AnnachiaraForino
* fname: ANNACHIARA
* lname: FORINO
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:08:21.202583
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
   input = raw_input # in python2, l'equivalente di input è raw_input


p = list(map(int, input().strip().split()))

def numero_di_inversioni(p):  
    for i in range(0, len(p)):
        if p[0]>p[1]:
            i+= 1
        return i
    for n in range(1, len(p)):
        
        if p[2]>p[3]:
        n +=1
           
    return n
    
    
    
    


print(numero_di_inversioni(p))
