"""
* user:  VR437327000
* fname: MADDALENA
* lname: BUSATTO
* task:  prova-game123-123
* score: 0.0
* date:  2019-02-27 10:55:16.102247
"""
#!/usr/bin/env python3
# Template di soluzione di game123_123

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def play(n1, n2): 
    a=0
    c=0
    if (n1+n2)%4==0:
        return (0,0)  
    elif n1>n2:
        c=4*n2
        a=c-(n1+n2)
        return (a, 0)
    elif n1<n2:
        c=4*n1
        a=c-(n1+n2)
        return (0, a)
    
# FINE area entro la quale ti richiediamo/consigliamo di operare.

n1 = int(input())
n2 = int(input())
togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)
