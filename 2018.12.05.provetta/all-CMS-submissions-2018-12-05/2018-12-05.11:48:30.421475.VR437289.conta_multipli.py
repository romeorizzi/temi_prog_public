"""
* user:  VR437289
* fname: ALVIANO
* lname: MASENELLI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:48:30.421475
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    w=0
    for i in range (1,c+1):
        if (i%a==0):
            if (i%b != 0):
                w=w+1
    return w
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
