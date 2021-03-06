"""
* user:  AnnachiaraForino
* fname: ANNACHIARA
* lname: FORINO
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:52:33.139030
"""
#!/usr/bin/env python3
#funzione che riceve in input tre numeri naturali a,b,c e ritorna il numero di quei numeri #interi positivi n
#dominio:numeri naturali a,b,c
#co-dominio:numeri interi positivi 
#pre-condizioni:numeri naturali>0, numero intero n <= c, a divide n, b non divide n. 
#post-condizioni:il programma deve ritornare il numero di multipli di a non divisibili per #b che non eccedano c




def conta_multipli(a, b, c):
    sol = 0
    i = 1
    m = 0
    if m<=b:
        while ((a*i)<=c):
            if(a*i) % b != 0:
                sol += 1
            i += 1
    else:
        b += b
    return sol
    
        
  
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
