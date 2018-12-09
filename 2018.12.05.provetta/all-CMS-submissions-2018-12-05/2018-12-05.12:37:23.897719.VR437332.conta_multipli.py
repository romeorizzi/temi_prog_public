"""
* user:  VR437332
* fname: LAURA
* lname: ZANI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:37:23.897719
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def conta_multipli(a, b, c):
    ret=0
    i=0
    while(i<=c):
        if((i%a)==0 ):
            if ((i%b!=0)):
                ret=ret+1
        i=i+1    
    return ret


a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))

#python conta_multipli_template_sol.py
