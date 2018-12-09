"""
* user:  VR429626
* fname: ARIANNA
* lname: PELLIZZARO
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 13:15:28.300326
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa è la funzione che devi perfezionare
    if n1==n2:
        return (0,0)   # non arrenderti sempre!
    elif n1>n2:
        return (n1-n2, 0)
    else:
        return (0, n2-n1)
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

