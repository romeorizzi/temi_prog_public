"""
* user:  VR437564
* fname: GIORDANO
* lname: CORBIOLI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:47:52.746454
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio


def conta_multipli(a, b, c):
    z=0
    
    for i in range (1,c+1):
        if (i%a==0):
            if (i%b !=0):
                z=z+1
       
    return z

# Lettura input: non devi modificare il codice sotto questa riga

a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
