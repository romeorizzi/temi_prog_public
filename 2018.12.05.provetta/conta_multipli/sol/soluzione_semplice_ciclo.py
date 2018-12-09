# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Alessandro Righi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def conta_multipli(a, b, c):
    count = 0
    for n in range(c+1):
        if n % a == 0 and n % b != 0:
            count += 1
    return count
    
a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))

