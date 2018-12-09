"""
* user:  VR437269
* fname: MATTEO
* lname: BONINI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 11:50:36.542316
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):

    if n1 > n2:
        return (n1-n2,0)
    else:
        return (0,n2-n1)

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

