"""
* user:  VR429685
* fname: SOFIA
* lname: RIZZOTTO
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:20:45.793220
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa č la funzione che devi perfezionare
    if n1>2:
        y=n1-2
    else:
        y=0
    if n2>2:
        x=n2-2
    else:
        x=0
    return (y,x)
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

