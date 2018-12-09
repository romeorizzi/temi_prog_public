"""
* user:  VR429625
* fname: GIOVANNI
* lname: LORENZI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:16:26.812416
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):
    if n1>n2:
        n1=n1-n2
        n2=0
    elif n2>n1:
        n2=n2-n1
        n1=0
    else:
        n1=0
        n2=0
    
    return (n1,n2)   # non arrenderti sempre!
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

