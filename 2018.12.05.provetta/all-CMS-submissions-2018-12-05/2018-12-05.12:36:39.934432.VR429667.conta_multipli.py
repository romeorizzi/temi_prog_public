"""
* user:  VR429667
* fname: FEDERICO
* lname: ZANCAN
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:36:39.934432
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    n = 1
    j = 0    
    
    while(n <= c):
        if (n % b != 0 and n % a == 0):
            j += 1
        n += 1    

    return j
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
