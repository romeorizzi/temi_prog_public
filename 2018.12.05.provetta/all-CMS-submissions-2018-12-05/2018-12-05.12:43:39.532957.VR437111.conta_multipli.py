"""
* user:  VR437111
* fname: LUCA
* lname: CHIAVEGATO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:43:39.532957
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    i=0
    for z in range(1,c+1):
       
       if z%a==0 and z%b!=0:
          i=i+1
    return i
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
