"""
* user:  VR429685
* fname: SOFIA
* lname: RIZZOTTO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:06:41.665046
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    x=0
    for i in range(1,c+1):
        if i%a==0 and i%b!=0:
            x += 1
    return x
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print (conta_multipli(a, b, c))
