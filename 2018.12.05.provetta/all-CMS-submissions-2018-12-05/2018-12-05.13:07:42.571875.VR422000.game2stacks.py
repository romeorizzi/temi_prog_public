"""
* user:  AnnachiaraForino
* fname: ANNACHIARA
* lname: FORINO
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 13:07:42.571875
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

n1=int(input())
n2=int(input())

def play(n1, n2):  
    togli1=0
    togli2=0
    if(n1>n2):
        togli1=n1-n2
    if(n2>n1):
        togli2=n2-n1
    return(togli1, togli2)
         

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

