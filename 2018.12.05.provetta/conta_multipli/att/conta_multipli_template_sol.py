# -*- coding: utf-8 -*-
# Template di soluzione per il problema conta_multipli

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

# INIZIO area entro la quale ti consigliamo di operare.

# Ecco la funzione che spetta a tè di implementare come da consegna dell'esercizio (ove credi puoi articolarla e scomporla su ulteriori funzioni e/o introdurre strutture dati di supporto):   
def conta_multipli(a, b, c):
    return 42

# FINE area entro la quale ti consigliamo di operare.

# Lettura input: all'esame non è il caso tu modifichi il codice sotto questa riga.    
a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))
