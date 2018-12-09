"""
* user:  VR429591
* fname: SARA
* lname: AVESANI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:13:31.947872
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    k=0
    for i in range(1,c+1):
        if i%a == 0 and i%b != 0:
            k=k+1
    return k
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
