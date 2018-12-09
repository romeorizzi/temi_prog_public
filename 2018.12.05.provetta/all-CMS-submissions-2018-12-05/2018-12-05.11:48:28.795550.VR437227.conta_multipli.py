"""
* user:  VR437227
* fname: DAVIDE
* lname: COPPOLA
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:48:28.795550
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    e=0
    for i in range(a,c+1):
        if i%a==0 and i%b!=0:
            e=e+1                
    return e
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
