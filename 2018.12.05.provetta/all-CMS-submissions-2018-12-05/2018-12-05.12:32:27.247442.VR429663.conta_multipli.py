"""
* user:  VR429663
* fname: DENNIS
* lname: MODESTI
* task:  conta_multipli
* score: 80.0
* date:  2018-12-05 12:32:27.247442
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    if a%b == 0:
        return 0
    return c//a - c//(a*b)
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print (conta_multipli(a, b, c))
