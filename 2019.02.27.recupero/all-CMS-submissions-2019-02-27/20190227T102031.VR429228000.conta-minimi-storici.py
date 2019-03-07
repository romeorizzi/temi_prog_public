"""
* user:  VR429228000
* fname: LUCA
* lname: COSI
* task:  prova-conta-minimi-storici
* score: 80.0
* date:  2019-02-27 10:20:31.490512
"""
#!/usr/bin/env python3
# Template di soluzione per conta_minimi_storici

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
    
def conta_minimi_storici_pari(st_list):
    s=len(st_list)
    i=0
    j=0
    count=0
    while(i<s):
        j=0
        t=True
        while(j<i):
            if st_list[j]<st_list[i]:
                t=False
            j=j+1
        if t==True:
            if (st_list[i]%2)==0:
                count=count+1
        i=i+1
            
        
    return count # risposta corretta ad esempio se tutti i numeri sono dispari

def conta_minimi_storici_dispari(st_list):
    s=len(st_list)
    i=0
    j=0
    count=0
    while(i<s):
        j=0
        t=True
        while(j<i):
            if st_list[j]<st_list[i]:
                t=False
            j=j+1
        if t==True:
            if (st_list[i]%2)!=0:
                count=count+1
        i=i+1
            
        
    return count
    
     # risposta corretta ad esempio se tutti i numeri sono pari

# FINE area entro la quale ti richiediamo/consigliamo di operare.
    
n, p = map(int, input().strip().split())
st_list = list(map(int, input().strip().split()))
assert len(st_list) == n >= 1
assert 0 <= p <= 1
if p == 0:
    print(conta_minimi_storici_pari(st_list))
else:
    print(conta_minimi_storici_dispari(st_list))
    

