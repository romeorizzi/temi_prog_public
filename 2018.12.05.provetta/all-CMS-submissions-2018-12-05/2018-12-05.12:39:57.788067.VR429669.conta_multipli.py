"""
* user:  VR429669
* fname: DAVIDE
* lname: CAMPONOGARA
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:39:57.788067
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
    soluzioni=0
    i=1
    while(a*i<=c):
        if((a*i)%b!=0):
            soluzioni+=1 
        i+=1   
    return soluzioni
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
