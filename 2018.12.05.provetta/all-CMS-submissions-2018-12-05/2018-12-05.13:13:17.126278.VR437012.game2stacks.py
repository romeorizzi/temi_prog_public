"""
* user:  VR437012
* fname: Giosue
* lname: Cavagna
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 13:13:17.126278
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(raw_input())
n2 = int(raw_input())

def play(n1, n2):  # questa č la funzione che devi perfezionare
    a=n1-n2
    if a==0:
        return(0,0)
    if a<0:
        return(0,n2+a)
    if a>0:
        return(a,0)

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

