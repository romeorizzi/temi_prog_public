"""
* user:  VR437909
* fname: ANNALISA
* lname: BONTEMPI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:52:31.355904
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    sol=0
    i=0
    m=0
    if m <= b:
        while ((a*b)<=c):
            if(a*I)%b !=0:
                sol += 1
            i += 1
    else:
        b += b
    return sol

# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
raw_
