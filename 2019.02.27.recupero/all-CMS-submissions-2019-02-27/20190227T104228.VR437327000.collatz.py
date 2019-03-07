"""
* user:  VR437327000
* fname: MADDALENA
* lname: BUSATTO
* task:  prova-collatz
* score: 100.0
* date:  2019-02-27 10:42:28.523680
"""
#!/usr/bin/env python3
# Template di soluzione di collatz

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def simulate(n):
    confs=[]
    if n==1:
        confs.append(n)
    else:
        confs.append(n)
        while (n>1):
            if n%2==0:
                n=n//2
                confs.append(n)
            elif (n%2 !=0):
                n=3*n+1
                confs.append(n)
    return confs

# FINE area entro la quale ti richiediamo/consigliamo di operare.

n = int(input())
for i in simulate(n):
    print(i)

