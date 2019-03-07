"""
* user:  VR437299000
* fname: ENRICO
* lname: MELEGATI
* task:  prova-conta-minimi-storici
* score: 0.0
* date:  2019-02-27 11:23:48.288262
"""
#!/usr/bin/env python3
# Template di soluzione per conta_minimi_storici

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
    
def conta_minimi_storici_pari(st_list):   # questa è una funzione che devi perfezionare/riscrivere
    return 0 # risposta corretta ad esempio se tutti i numeri sono dispari

def conta_minimi_storici_dispari(st_list):  # questa è una funzione che devi perfezionare/riscrivere
    return 0 # risposta corretta ad esempio se tutti i numeri sono pari

# FINE area entro la quale ti richiediamo/consigliamo di operare.
    
n, p = map(int, input().strip().split())
st_list = list(map(int, input().strip().split()))
assert len(st_list) == n >= 1
assert 0 <= p <= 1
if p == 0:
    print(conta_minimi_storici_pari(st_list))
else:
    print(conta_minimi_storici_dispari(st_list))
    

