"""
* user:  VR429684
* fname: ERIKA
* lname: ZOCCATELLI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:05:16.371951
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa è la funzione che devi perfezionare
    a=0
    b=0
    if(n1<n2):
        b=n2-n1
    if(n1>n2):
        a=n1-n2        
    return (a,b)   # non arrenderti sempre!
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

