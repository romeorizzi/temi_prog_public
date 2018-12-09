"""
* user:  VR437077
* fname: FABIO
* lname: MARINI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 11:49:42.955427
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    n = 1
    conta = 0
    while n <= c:
        if (n%a == 0) and (n%b != 0):
            conta += 1
        n += 1


    return conta
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
