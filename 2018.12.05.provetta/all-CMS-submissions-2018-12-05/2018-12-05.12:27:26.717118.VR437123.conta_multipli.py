"""
* user:  VR437123
* fname: ISOTTA
* lname: CARAVAGGI
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:27:26.717118
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
	x=0
	for n in range (a, c+1):
		if ((n%a)==0) & ((n%b)!=0):
			x=x+1 
	return x
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
