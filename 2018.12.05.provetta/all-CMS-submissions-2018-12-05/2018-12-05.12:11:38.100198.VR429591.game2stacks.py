"""
* user:  VR429591
* fname: SARA
* lname: AVESANI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:11:38.100198
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2): 
    togli1=0
    togli2=0 
    if n1==n2:
        togli1=0
        togli2=0
    elif n1>n2:
        togli1=(n1-n2)
        togli2=0
    else:
        togli1=0
        togli2=(n2-n1)

    print (togli1)
    print (togli2)

play(n1, n2)
    



