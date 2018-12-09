"""
* user:  VR429705
* fname: MATTIA
* lname: BOMBIERI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:49:16.306054
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
    
a, b, c = map(int, input().split())
def conta_multipli(a, b, c):
    m = 0
    for n in range(1, c+1):
        if n % a == 0 and n % b != 0:
            m = m + 1
    return m
print(conta_multipli(a, b, c))
