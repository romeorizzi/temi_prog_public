"""
* user:  VR429684
* fname: ERIKA
* lname: ZOCCATELLI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:00:00.548567
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    n=a 
    m=0   
    while(n<=c):
        if(n%a==0)&(n%b!=0):
            m=m+1
        n=n+1      
    return m
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
