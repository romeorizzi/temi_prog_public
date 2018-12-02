#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Soluzione di perm_recognition, written by Romeo Rizzi 2018.11.28

MINORE = -1
UGUALE = 0
MAGGIORE = 1

s = input()
t = input()
assert len(s) > 0
assert len(t) > 0

def lex_compare(s,t):
    if len(s) == 0 and len(t) == 0:
        return UGUALE
    if len(s) == 0:
        return MINORE
    if len(t) == 0:
        return MAGGIORE
    if s[0]<t[0]:
        return MINORE
    if s[0]>t[0]:
        return MAGGIORE
    return lex_compare(s[1:],t[1:])

print( lex_compare(s,t) )

