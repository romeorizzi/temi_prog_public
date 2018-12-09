"""
* user:  VR437564
* fname: GIORDANO
* lname: CORBIOLI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:50:48.242678
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):
    if (n1==n2):
        x=0
        y=0    
    if (n1>n2):
        x=n1-n2
        y=0
    if (n1<n2):
        y=n2-n1 
        x=0 
    return (x,y)   
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

