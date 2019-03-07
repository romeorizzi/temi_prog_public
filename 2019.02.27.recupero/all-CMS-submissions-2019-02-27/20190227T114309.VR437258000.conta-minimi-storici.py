"""
* user:  VR437258000
* fname: Giulia
* lname: Carrodano
* task:  prova-conta-minimi-storici
* score: 0.0
* date:  2019-02-27 11:43:09.705283
"""
#!/usr/bin/env python3

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
def conta_minimi_storici_pari(st_list):
    m=[]
    for i in range (0,len (st_list)):
	    if st_list[i]<st_list[i-1]:
              if st_list[i]%2==0:
		         m=m+st_list[i]
    return len (m)
    

def conta_minimi_storici_dispari(st_list):  
    n=[]
    for i in range (0,len (st_list)):
	    if st_list[i]<st_list[i-1]:
                if not (st_list[i]%2==0):
		             n=n+st_list[i]
    return len (n)

# FINE area entro la quale ti richiediamo/consigliamo di operare.
    
n, p = map(int, input().strip().split())
st_list = list(map(int, input().strip().split()))
assert len(st_list) == n >= 1
assert 0 <= p <= 1
if p == 0:
    print(conta_minimi_storici_pari(st_list))
else:
    print(conta_minimi_storici_dispari(st_list))
    
