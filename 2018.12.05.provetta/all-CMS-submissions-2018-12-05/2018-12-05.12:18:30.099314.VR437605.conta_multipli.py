"""
* user:  VR437605
* fname: ANNALISA
* lname: DETTORI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:18:30.099314
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
    p=0
    for n in range (1,c+1):
        if n%a==0 and n%b!=0 :
            p+=1
    return p
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
