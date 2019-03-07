"""
* user:  VR429228000
* fname: LUCA
* lname: COSI
* task:  prova-perm-composition
* score: 0.0
* date:  2019-02-27 10:22:49.896314
"""
#!/usr/bin/env python3
# Template di soluzione per perm_composition

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
    
def perm_composition(p1, p2):
    s=[]
    l=len(p1)
    k=0
    i=0
    while i<l:
        k=p1[i]
        s.append[k]
        i=i+1
        

    return s # devi implementare qui la funzione richiesta
    
# FINE area entro la quale ti richiediamo/consigliamo di operare.

# codice di valutazione, non devi modificare nulla sotto questo commento
N = int(input())
p1 = list(map(int, input().strip().split()))
p2 = list(map(int, input().strip().split()))
assert len(p1) == N
assert len(p2) == N
print(*perm_composition(p1, p2))

