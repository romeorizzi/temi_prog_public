"""
* user:  VR437373
* fname: MARCO
* lname: QUANILLI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:34:13.307594
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    i=a
    l=0
    while(i<=c):
        if(i%a==0):
            if(i%b!=0):
                l=l+1 
        i=i+1
    return l      
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
