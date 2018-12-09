"""
* user:  VR429670
* fname: ENRICO
* lname: NEGRO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:36:08.946857
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio

def conta_multipli(a, b, c):
    x=0
    i=0
    while(a*i<=c):
        if (a*i%b!=0):
            x=x+1
        i=i+1
    return x

# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
