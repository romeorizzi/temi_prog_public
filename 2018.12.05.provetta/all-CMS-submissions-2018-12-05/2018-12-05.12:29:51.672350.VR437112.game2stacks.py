"""
* user:  VR437112
* fname: ALESSANDRO
* lname: SIGNORETTO
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:29:51.672350
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):
     if (n1==n2):
    return (0,0)   # non arrenderti sempre!
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

