"""
* user:  VR437468
* fname: MATTEO
* lname: D'ALESSANDRO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:15:58.747975
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

#introduco una nuova funzione per calcolare il minimo comune multiplo
def mcm(a,b): 
    for i in range(a,a*(b+1),a):
        if (i%b==0):
            break
    return i
            
def conta_multipli(a, b, c):
    return int(c/a)-int(c/(mcm(a,b)))
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a,b,c))

