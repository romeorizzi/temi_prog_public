"""
* user:  VR439308
* fname: Gaia
* lname: Dalla Benetta
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:14:58.019846
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    n=0
    for i in range (n+1):
        if (a % n == 0):                
            if (n % b != 0):
                        n=n
            else:
                n=n+1


    return 42
    
# Lettura raw_input: non devi modificare il codice sotto questa riga
a, b, c= map(int,input().split())
print(conta_multipli(a, b, c))
