#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Template di soluzione di collatz

from __future__ import print_function, division
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input


# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def simulate(n):
    confs = []
    while n > 1:
        confs.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n +1
    confs.append(1)
    return confs

# FINE area entro la quale ti richiediamo/consigliamo di operare.

n = int(input())
for i in simulate(n):
    print(i)

