"""
* user:  VR429713
* fname: MICHELA
* lname: PAGLIARINI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 11:58:50.993939
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    multipli=0
    for n in range (1,c+1):
        if n%a == 0 and n%b != 0 :
            multipli+=1
    return multipli
            
        


    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
