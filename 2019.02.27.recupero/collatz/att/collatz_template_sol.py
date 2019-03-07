#!/usr/bin/env python3
# Template di soluzione di collatz

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def simulate(n):
    confs = []
    confs.append(5)
    confs.append(16)
    confs.append(8)
    confs.append(4)
    confs.append(2)
    confs.append(1)
    return confs

# FINE area entro la quale ti richiediamo/consigliamo di operare.

n = int(input())
for i in simulate(n):
    print(i)

