#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Tempate di soluzione per il problema perm_recognition, written by Romeo Rizzi 2018.11.28


n = int(input())
f = list( map( int, input().split() ) )
assert len(f) == n

def is_perm(f):    # questa è la funzione che devi perfezionare
    return True    # ma non sempre f codifica una permutazione!

print( is_perm(f) )

