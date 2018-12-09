"""
* user:  VR437210
* fname: JACOPO
* lname: QUIRINALI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:51:47.465101
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    risultato = 0    
    cont = a 
    while (cont<=c):
        if (cont%a==0):
            if(cont%b!=0):
                risultato = risultato+1  
                print(cont)  
        cont=cont+1
    return (risultato)
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
