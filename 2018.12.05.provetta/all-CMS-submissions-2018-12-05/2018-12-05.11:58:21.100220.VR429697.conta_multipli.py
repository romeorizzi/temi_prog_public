"""
* user:  VR429697
* fname: GABRIELE
* lname: BALDO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 11:58:21.100220
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    m=0
    for i in range(a, (c+1)):
        if i%a==0 and i%b!=0:
            m=m+1
    return m

# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))    


    
