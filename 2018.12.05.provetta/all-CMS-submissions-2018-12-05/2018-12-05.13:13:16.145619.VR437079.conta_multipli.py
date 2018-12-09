"""
* user:  VR437079
* fname: GIULIA
* lname: ALTOBEL
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 13:13:16.145619
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_inpu
# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    p=0
    for i in range (a,c+1):
        if i%a==0 and i%b!=0:
            p=p+1
    return p         
         
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
