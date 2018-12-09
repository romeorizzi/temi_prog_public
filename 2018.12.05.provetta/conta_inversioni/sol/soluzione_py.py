# -*- coding: utf-8 -*-
# Soluzione di conta_inversioni, written by Andrea Cracco 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    sol = 0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]:
                sol += 1
    return sol

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
