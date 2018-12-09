"""
* user:  VR429690
* fname: ALBERTO
* lname: AMBROSI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:48:08.258171
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    out=0
    for i in range(c+1):
        if i%a==0 and i%b!=0:
            out=out+1
    return out
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
