"""
* user:  VR429718
* fname: GIADA
* lname: SOSO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 13:08:17.169727
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    n=0
    for i in range(0,c+1):
        if n%a==0:
            if n%b!=0:
                n=n+1
    return n
  
  
    



    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
