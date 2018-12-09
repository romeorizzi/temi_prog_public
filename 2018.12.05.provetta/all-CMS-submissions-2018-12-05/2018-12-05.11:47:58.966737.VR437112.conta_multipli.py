"""
* user:  VR437112
* fname: ALESSANDRO
* lname: SIGNORETTO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:47:58.966737
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    n=0
    i=1
    while ((a*i)<=c):
     if not ((a*i)%b==0):
        n=n+1
     i=i+1
    return n
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
