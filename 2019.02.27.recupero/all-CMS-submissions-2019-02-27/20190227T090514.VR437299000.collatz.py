"""
* user:  VR437299000
* fname: ENRICO
* lname: MELEGATI
* task:  prova-collatz
* score: 0.0
* date:  2019-02-27 09:05:14.499288
"""
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

