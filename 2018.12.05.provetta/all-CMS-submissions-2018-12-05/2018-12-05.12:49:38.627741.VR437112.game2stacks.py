"""
* user:  VR437112
* fname: ALESSANDRO
* lname: SIGNORETTO
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:49:38.627741
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):
     a=0
     if (n1==n2):
      n=(0,0)
     if (n1>n2):
      n=((n1%n2),0)
     if (n2>n1):
      n=(0,(n1%n2))
     return n
      
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

