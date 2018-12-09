"""
* user:  VR429669
* fname: DAVIDE
* lname: CAMPONOGARA
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:38:26.841711
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    soluzioni=0
    i=1
    while(a*i<=c):
        if((a*i)%b!=0):
            soluzioni+=1 
        i+=1   
    return soluzioni
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
