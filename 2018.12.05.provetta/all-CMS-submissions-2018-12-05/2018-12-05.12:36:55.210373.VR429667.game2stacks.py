"""
* user:  VR429667
* fname: FEDERICO
* lname: ZANCAN
* task:  game2stacks
* score: 90.0
* date:  2018-12-05 12:36:55.210373
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())

def play(n1, n2):   # questa è la funzione che devi perfezionare

    if(n1 == 1 or n2 == 1 ):
        return (0,0)   # non arrenderti sempre!

    elif n1 == n2:
        return (0,0)
    
    elif n1 > n2:
        return((n1-n2),0)
    
    elif n1 < n2:
        return (0,(n2-n1))
        


    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

