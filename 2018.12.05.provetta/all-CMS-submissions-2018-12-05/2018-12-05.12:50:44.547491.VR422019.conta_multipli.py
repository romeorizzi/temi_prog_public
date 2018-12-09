"""
* user:  LucaFaccioli
* fname: LUCA
* lname: FACCIOLI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:50:44.547491
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
    sol = 0
    i = 1
    m=0
    if a > 0:
        if m<=b:
            while ((a*i)<=c):
                if (a*i) % b != 0:
                    sol +=1
                i += 1
        else:   
            b +=b
            
            
        
    return sol
            

    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
