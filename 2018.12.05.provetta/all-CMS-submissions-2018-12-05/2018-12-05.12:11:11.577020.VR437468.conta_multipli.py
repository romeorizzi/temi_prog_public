"""
* user:  VR437468
* fname: MATTEO
* lname: D'ALESSANDRO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:11:11.577020
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    mul=0
    for i in range (a,c+1,a):
        if (i%b!=0):
            mul=mul+1
    return mul
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
