"""
* user:  VR437327000
* fname: MADDALENA
* lname: BUSATTO
* task:  prova-collatz
* score: 0.0
* date:  2019-02-27 09:54:50.832834
"""
#!/usr/bin/env python3
# Template di soluzione di collatz

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def simulate(n):
    confs= []
    if n==1:
        confs.append(n)
    else:
        while (n>1):
            #print(n)
            #print("ciao",n)
            #risp = input("premi invio")
            #print("hai iserito",risp)
            if n%2==0:
                n=n/2
                confs.append(n)
            elif (n%2 !=0):
                n=3*n+1
                confs.append(n)
            #print("addio",n)
    return confs

# FINE area entro la quale ti richiediamo/consigliamo di operare.

n = int(input())
for i in simulate(n):
    print(i)

