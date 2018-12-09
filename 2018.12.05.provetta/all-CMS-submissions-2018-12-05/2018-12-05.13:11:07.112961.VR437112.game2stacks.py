"""
* user:  VR437112
* fname: ALESSANDRO
* lname: SIGNORETTO
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 13:11:07.112961
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):
    tolgi1=0
    togli2=0
    if (n1>n2):
      togli1=n1-n2
    if (n2>n1):
      togli2=n2-n1
    return (tolgi1,togli2)
      
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

