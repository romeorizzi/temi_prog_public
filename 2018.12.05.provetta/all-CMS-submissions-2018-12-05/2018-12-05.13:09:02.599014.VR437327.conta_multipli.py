"""
* user:  VR437327
* fname: MADDALENA
* lname: BUSATTO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 13:09:02.599014
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    b=0
    p=1
    for i in range (a, c+1):
        if a%i==0 and i%b!=0:
            b=b+1
            
    return i
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
