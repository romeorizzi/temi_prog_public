"""
* user:  VR429714
* fname: DOMENICO
* lname: DI GRAZIA
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 11:55:02.504389
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    d=0
    for n in range(1, c+1):
        if n%a==0 and n%b!=0:
            d=d+1   
    return d
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
