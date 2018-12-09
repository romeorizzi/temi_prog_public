"""
* user:  VR437011
* fname: SARA
* lname: QUINTO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:46:01.054115
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio


def conta_multipli(a, b, c):
    k = 0
    for n in range (1, c+1):
       if n%a == 0 and n%b != 0:
            k = k+1 
    return k


    
        
           
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
