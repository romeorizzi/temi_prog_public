"""
* user:  VR437168
* fname: GIACOMO
* lname: SCHIESARI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:47:38.592042
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    n = 0
    for i in range(a,c+1):
        if i%a == 0 and i%b!=0:
            n = n +1
    return n
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
