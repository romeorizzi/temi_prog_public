"""
* user:  VR437332
* fname: LAURA
* lname: ZANI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:56:24.727031
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28

n1 = int(input())
n2 = int(input())
def play(n1, n2):
    if (n1==n2):
        if (n1<2):            
            return (0,0)   #non ho piu alcuna possibita di vincere
        else:
            return (0,(n1-n1))   #faccio in modo che rimangano n1 e 1 pedina
    else:
        if(n1<n2):
            if (n1==0):
                return (0, n2)  #vinco sempre
            else:    
                return (0,(n2-n1))   # spero in una mossa sbagliata del mio avversario
        else:#se n2<n1
            if (n2==0):
                return (n1,0)   #vinco sempre
            else:
                return ((n1-n2), 0)
             

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

