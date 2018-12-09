"""
* user:  VR437208
* fname: NICOLE
* lname: CORSO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 13:04:51.734971
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input





def conta_multipli(a, b, c):
    k=0

    for i in range(1,c+1):
        
        if i%a==0 and i%b!=0:
            k=k+1
    return k
        
        
        
    
    
        
       
        
            


# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
