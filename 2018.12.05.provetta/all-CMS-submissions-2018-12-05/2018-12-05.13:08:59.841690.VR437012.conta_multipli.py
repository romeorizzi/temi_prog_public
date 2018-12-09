"""
* user:  VR437012
* fname: Giosue
* lname: Cavagna
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 13:08:59.841690
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def divide (n, d):
    if n%d == 0:
        return True
    return False

def conta_multipli(a, b, c):
    n=1  
    res=0  
    while n<=c:
        if divide(n,a):
            res=res+1
            if divide(n,b):
                res=res-1
        n=n+1
    return res

    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
