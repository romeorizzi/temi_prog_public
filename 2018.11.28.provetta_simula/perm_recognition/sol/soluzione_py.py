#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Soluzione di perm_recognition, written by Romeo Rizzi 2018.11.28

n = int(input())
f = list( map( int, input().strip().split() ) )
assert len(f) == n

def is_perm(f):
    n = len(f)
    seen = [False] * n
    for a in f:
        if a < 0 or a >= n:
            return False
        if seen[a]:
            return False
        seen[a] = True
    return True 
    
print( is_perm(f) )

