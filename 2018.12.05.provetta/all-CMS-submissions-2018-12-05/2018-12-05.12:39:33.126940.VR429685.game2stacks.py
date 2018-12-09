"""
* user:  VR429685
* fname: SOFIA
* lname: RIZZOTTO
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:39:33.126940
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa č la funzione che devi perfezionare
    x=0    
    if n1>=n2:
        while n1!=n2:
            n2=n2+1
            x += 1
        return (x,0)
    if n2>n1:
        while n1!=n2:
            n1=n1+1
            x += 1
        return (0,x)

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

