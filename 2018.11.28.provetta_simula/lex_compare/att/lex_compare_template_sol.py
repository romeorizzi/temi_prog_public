#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di lex_compare, written by Romeo Rizzi 2018.11.28

MINORE = -1
UGUALE = 0
MAGGIORE = 1

s = input().strip()
t = input().strip()
assert len(s) > 0
assert len(t) > 0

def lex_compare(s,t):   # questa è la funzione che devi perfezionare 
    return UGUALE       # risposta corretta solo nel caso le due stringhe siano uguali

print( lex_compare(s,t) )

