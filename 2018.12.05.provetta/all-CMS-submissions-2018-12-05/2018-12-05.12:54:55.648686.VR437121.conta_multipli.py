"""
* user:  VR437121
* fname: PIETRO
* lname: GIOVANNONI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:54:55.648686
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
    m=0
    for i in range(a, c+1):
        if (i%a)==0 and (i%b)!=0:
            m=m+1
    return m
     
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
