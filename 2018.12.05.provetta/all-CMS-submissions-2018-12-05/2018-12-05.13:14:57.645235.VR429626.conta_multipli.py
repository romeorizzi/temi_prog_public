"""
* user:  VR429626
* fname: ARIANNA
* lname: PELLIZZARO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 13:14:57.645235
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli (a, b, c):
    n=1
    s=0
    while (a*n)<=c:
        if ((a*n)%b)!=0:
            s+=1
        n+=1
    return s
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
