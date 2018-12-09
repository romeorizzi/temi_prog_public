"""
* user:  VR429625
* fname: GIOVANNI
* lname: LORENZI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:58:28.949652
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    risposta=0
    n=1
    while n<=c:
        if n%a==0 :
            if n%b!=0:
                risposta+=1
        n=n+1
    return risposta
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
