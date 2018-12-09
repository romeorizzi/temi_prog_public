"""
* user:  VR429871
* fname: MARCO
* lname: GHIOTTO
* task:  conta_multipli
* score: 80.0
* date:  2018-12-05 12:19:05.848599
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
		for count in range (1, c+1):
			if ((count%a)==0) & ((count%b)!=0):
				x=x+1
	return x
			
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, raw_input().split())
print(conta_multipli(a, b, c))
