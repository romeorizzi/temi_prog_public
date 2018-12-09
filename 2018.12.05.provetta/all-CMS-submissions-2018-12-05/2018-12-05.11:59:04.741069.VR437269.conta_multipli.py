"""
* user:  VR437269
* fname: MATTEO
* lname: BONINI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 11:59:04.741069
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    count = 0
    n = 1
    while n <= c :
        if (n%a==0)&(n%b!=0):
            count = count + 1
        n = n +1
    return count
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
