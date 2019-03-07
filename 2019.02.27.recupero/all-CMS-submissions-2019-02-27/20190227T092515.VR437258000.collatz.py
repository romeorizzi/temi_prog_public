"""
* user:  VR437258000
* fname: Giulia
* lname: Carrodano
* task:  prova-collatz
* score: 0.0
* date:  2019-02-27 09:25:15.462726
"""
#!/usr/bin/env python3

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def simulate(n):
    confs = [n]
    while not (n==1):
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    confs.append(n)
    return confs

# FINE area entro la quale ti richiediamo/consigliamo di operare.

n = int(input())
for i in simulate(n):
    print(i)
