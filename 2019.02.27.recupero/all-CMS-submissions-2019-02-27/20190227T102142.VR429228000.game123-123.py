"""
* user:  VR429228000
* fname: LUCA
* lname: COSI
* task:  prova-game123-123
* score: 100.0
* date:  2019-02-27 10:21:42.906612
"""
#!/usr/bin/env python3
# Template di soluzione di game123_123

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def play(n1, n2):
    a=0
    b=0
    if n1!=n2:
        if n1>n2:
            a=(n1-n2)%4
        else:
            b=(n2-n1)%4

    return (a,b)   # non arrenderti sempre!
    
# FINE area entro la quale ti richiediamo/consigliamo di operare.

n1 = int(input())
n2 = int(input())
togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

