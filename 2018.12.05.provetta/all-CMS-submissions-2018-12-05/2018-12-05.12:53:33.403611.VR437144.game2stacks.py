"""
* user:  VR437144
* fname: SIMONE
* lname: SORGATO
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:53:33.403611
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa è la funzione che devi perfezionare
    b=int(0)
    a=int(0)   
    if (n1>n2):
        b=n1-n2
        a=0
    if (n2>n1):
        a=n2-n1
        b=0
    if (n2==n1):
        return (0, 0)
    return (b,a)   # non arrenderti sempre!
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

