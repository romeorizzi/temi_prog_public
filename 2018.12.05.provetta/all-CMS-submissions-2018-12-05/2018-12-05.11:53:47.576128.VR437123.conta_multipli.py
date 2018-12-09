"""
* user:  VR437123
* fname: ISOTTA
* lname: CARAVAGGI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:53:47.576128
"""
#!/usr/bin/env python3
# Template per soluzione conta_multipli

# Devi modificare l'implementazione di questa funzione per fare 
# quanto richiesto dal testo dell'esercizio
def conta_multipli(a, b, c):
	x=0
	if a==c:
		x=x+1
	else:
		for n in range (1, c+1):
			if ((n%a)==0) & ((n%b)!=0):
				x=x+1 
	return x
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
