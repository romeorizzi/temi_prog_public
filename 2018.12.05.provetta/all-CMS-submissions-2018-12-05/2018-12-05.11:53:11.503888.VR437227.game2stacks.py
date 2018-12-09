"""
* user:  VR437227
* fname: DAVIDE
* lname: COPPOLA
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 11:53:11.503888
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa è la funzione che devi perfezionare
    togli1=0
    togli2=0
    if n1>n2:
        togli1=n1-n2
    if n1<n2:
        togli2=n2-n1
    return (togli1,togli2)   # non arrenderti sempre!
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

