"""
* user:  VR437144
* fname: SIMONE
* lname: SORGATO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:52:54.240193
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    z=int(a)
    n=int(0)
    while (z<=c):
        if (z%a==0):
            n=n+1
            z=z+1
        else:
            z=z+1
        if (z%b==0):
            z=z+1
    return n

    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
