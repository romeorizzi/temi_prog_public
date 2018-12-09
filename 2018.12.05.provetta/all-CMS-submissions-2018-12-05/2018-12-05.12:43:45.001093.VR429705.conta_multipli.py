"""
* user:  VR429705
* fname: MATTIA
* lname: BOMBIERI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:43:45.001093
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    return 42

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
