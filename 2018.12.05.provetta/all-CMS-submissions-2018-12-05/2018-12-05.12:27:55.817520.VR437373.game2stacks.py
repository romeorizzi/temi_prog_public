"""
* user:  VR437373
* fname: MARCO
* lname: QUANILLI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:27:55.817520
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):
    if(n1==n2):
        return (0,0)
    else:
        if(n1>n2):
            a=n1-n2
            return (a,0)
        else:
            b=n2-n1
            return (0,b)
                

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

