"""
* user:  VR437332
* fname: LAURA
* lname: ZANI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:44:39.053066
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    conta=0
    j=0
    i=0
    while (i<len(p)):
        j=i+1
        while (j<len(p)):
            if(p[i]>p[j]):
                conta=conta+1
            j=j+1
        i=i+1
        
    return conta

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))

#python conta_inversioni_template_sol.py
