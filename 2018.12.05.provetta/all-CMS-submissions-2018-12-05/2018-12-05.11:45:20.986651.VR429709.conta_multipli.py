"""
* user:  VR429709
* fname: DAVIDE
* lname: FORNARI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:45:20.986651
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    i=1
    n=0
    while (a*i<=c):
        if(((a*i)%b)!=0):
            n+=1
        i+=1
    return n
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
