"""
* user:  VR437011
* fname: SARA
* lname: QUINTO
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 13:08:07.494866
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):
    if n1 == n2:
        x = 0
        y = 0
    elif n1 > n2:
        x = n1 - n2
        y = 0
    elif n1 < n2:
        x = 0
        y = n2 - n1
    return (x,y)
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)
