"""
* user:  VR437258000
* fname: Giulia
* lname: Carrodano
* task:  prova-game123-123
* score: 0.0
* date:  2019-02-27 10:39:34.918656
"""
#!/usr/bin/env python3
# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
def play(n1, n2):  
    t1=0
    t2=0
    if not ((n1+n2)%4==0):
        if n1>=n2:
            t1=(n1+n2)%4
        else:
            t2=(n1+n2)%4

    return (t1,t2)   
    
# FINE area entro la quale ti richiediamo/consigliamo di operare.

n1 = int(input())
n2 = int(input())
togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

