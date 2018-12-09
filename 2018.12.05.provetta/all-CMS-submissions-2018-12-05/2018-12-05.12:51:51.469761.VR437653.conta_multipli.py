"""
* user:  VR437653
* fname: LUCA
* lname: PESERICO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:51:51.469761
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
    div=0    
    n=1    
    while n<=c:
        if n%a==0:
            div=div+1 
            if n%b==0:
                div=div-1
        n=n+1
    return div
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
