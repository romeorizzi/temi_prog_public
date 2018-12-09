"""
* user:  VR437373
* fname: MARCO
* lname: QUANILLI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:41:46.710241
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
    
def conta_multipli(a, b, c):
    i=a
    l=0
    while(i<=c):
        if(i%a==0):
            if(i%b!=0):
                l=l+1 
        i=i+1
    return l      
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
