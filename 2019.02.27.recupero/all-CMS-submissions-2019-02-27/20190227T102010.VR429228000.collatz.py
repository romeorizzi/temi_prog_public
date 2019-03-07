"""
* user:  VR429228000
* fname: LUCA
* lname: COSI
* task:  prova-collatz
* score: 100.0
* date:  2019-02-27 10:20:10.303181
"""
#!/usr/bin/env python3
# Template di soluzione di collatz

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def simulate(n):
    confs = [n]
    N=n
    while(N>1):
        if (N%2)==0:
            N=N//2
        else:
            N=1+3*N
        confs.append(N)
    return confs



# FINE area entro la quale ti richiediamo/consigliamo di operare.

n = int(input())
for i in simulate(n):
    print(i)

