"""
* user:  VR437327000
* fname: MADDALENA
* lname: BUSATTO
* task:  prova-conta-minimi-storici
* score: 20.0
* date:  2019-02-27 12:13:00.584832
"""
#!/usr/bin/env python3
# Template di soluzione per conta_minimi_storici

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
    
def conta_minimi_storici_pari(st_list):   # questa e' una funzione che devi perfezionare/riscrivere
    c=0
    if int(st_list[0])%2==0:
        c=1
    else:
        c=0
        for i in range (1, len(st_list)):
            for k in range (i-1, len(st_list)):
                if (((int(st_list[i])%2==0)) and ((int(st_list[k])%2==0))) and (int(st_list[i])<int(st_list[k])):
                    c=c+1               
    return c  # risposta corretta ad esempio se tutti i numeri sono dispari

def conta_minimi_storici_dispari(st_list):  # questa e' una funzione che devi perfezionare/riscrivere
    c=0
    if int(st_list[0])%2==0:
        c=0
    else:
        c=1
        for i in range (1,len(st_list)):
            for k in range (i-1, len(st_list)):
                if ((int(st_list[i])%2!=0) and (int(st_list[k])%2!=0))  and (int(st_list[i])<int(st_list[k13])):
                    c=c+1                
    return c
    
# FINE area entro la quale ti richiediamo/consigliamo di operare.
    
n, p = map(int, input().strip().split())
st_list = list(map(int, input().strip().split()))
assert len(st_list) == n >= 1
assert 0 <= p <= 1
if p == 0:
    print(conta_minimi_storici_pari(st_list))
else:
    print(conta_minimi_storici_dispari(st_list))
    

