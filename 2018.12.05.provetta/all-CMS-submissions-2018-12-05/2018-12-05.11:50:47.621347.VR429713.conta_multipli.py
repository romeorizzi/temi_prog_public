"""
* user:  VR429713
* fname: MICHELA
* lname: PAGLIARINI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:50:47.621347
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    multipli=0
    while n <=c:
        if n%a == 0 and n%b != 0 :
            multipli+=1
    return multipli
            
        


    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
