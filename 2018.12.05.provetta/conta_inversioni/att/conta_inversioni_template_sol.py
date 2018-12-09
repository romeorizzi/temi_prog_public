# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def numero_di_inversioni(p):
    return 42

# FINE area entro la quale ti richiediamo/consigliamo di operare.

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
