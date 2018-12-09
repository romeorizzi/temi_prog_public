"""
* user:  VR437208
* fname: NICOLE
* lname: CORSO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 13:01:29.051034
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio





def conta_multipli(a, b, c):
    k=0

    for i in range(1,c+1):
        
        if i%a==0 and i%b!=0:
            k=k+1
    return k
        
        
        
    
    
        
       
        
            


# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
