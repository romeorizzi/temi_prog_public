"""
* user:  VR437210
* fname: JACOPO
* lname: QUIRINALI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:58:16.886707
"""
# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input
def conta_multipli(a, b, c):
    risultato = 0    
    cont = a 
    while (cont<=c):
        if (cont%a==0):
            if(cont%b!=0):
                risultato = risultato+1  
        cont=cont+1
    return (risultato)
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
