"""
* user:  VR437112
* fname: ALESSANDRO
* lname: SIGNORETTO
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:56:50.495495
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
      z=(n1%n2)
      m=(z+n2)
      n=(m,0)
     if (n1<n2):
      x=(n2%n1)
      y=(x+n1)
      n=(0,y)
     return n
      
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

