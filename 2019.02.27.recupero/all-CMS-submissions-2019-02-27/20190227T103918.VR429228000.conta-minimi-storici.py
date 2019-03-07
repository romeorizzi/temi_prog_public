"""
* user:  VR429228000
* fname: LUCA
* lname: COSI
* task:  prova-conta-minimi-storici
* score: 100.0
* date:  2019-02-27 10:39:18.837281
"""
#!/usr/bin/env python3
# Template di soluzione per conta_minimi_storici

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
    
def conta_minimi_storici_pari(st_list):
    count=0
    if (st_list[0]%2)==0:
        count=count+1
    i=1
    l=len(st_list)
    m=st_list[0]
    while (i<l):
        if st_list[i]<m:
            if (st_list[i]%2)==0:
                count=count+1
            m=st_list[i]
        i=i+1
    return count # risposta corretta ad esempio se tutti i numeri sono dispari

def conta_minimi_storici_dispari(st_list):
    count=0
    if (st_list[0]%2)!=0:
        count=count+1
    i=1
    l=len(st_list)
    m=st_list[0]
    while (i<l):
        if st_list[i]<m:
            if (st_list[i]%2)!=0:
                count=count+1
            m=st_list[i]
        i=i+1
    return count

# FINE area entro la quale ti richiediamo/consigliamo di operare.
    
n, p = map(int, input().strip().split())
st_list = list(map(int, input().strip().split()))
assert len(st_list) == n >= 1
assert 0 <= p <= 1
if p == 0:
    print(conta_minimi_storici_pari(st_list))
else:
    print(conta_minimi_storici_dispari(st_list))
    

