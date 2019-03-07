#!/usr/bin/env python3
# Template di soluzione per perm_composition

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
    
def perm_composition(p1, p2):
    return [0]*len(p1) # devi implementare qui la funzione richiesta
    
# FINE area entro la quale ti richiediamo/consigliamo di operare.

# codice di valutazione, non devi modificare nulla sotto questo commento
N = int(input())
p1 = list(map(int, input().strip().split()))
p2 = list(map(int, input().strip().split()))
assert len(p1) == N
assert len(p2) == N
print(*perm_composition(p1, p2))

