"""
* user:  VR437299000
* fname: ENRICO
* lname: MELEGATI
* task:  prova-conta-minimi-storici
* score: 0.0
* date:  2019-02-27 12:14:16.491984
"""
#!/usr/bin/env python3
# Template di soluzione per conta_minimi_storici

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.
    
def conta_minimi_storici(lista,p):  # questa è una funzione che devi perfezionare/riscrivere
    assert 0 <= p <= 1
    n = len(lista)
    a=0
    b=1
    i=0
    if n >= 1:
      if p == 0:
          if lista[a]%2==0:
              while lista[a]>lista[b] and lista[a]%2==0 and lista[b]%2==0:
                 a=b
                 b=b+1
                 i=i+1
              b=b+1
              print(i)
      else:
             if lista[a]>lista[b] :
                 a=b
                 b=b+1
                 i=i+1
    return i # risposta corretta ad esempio se tutti i numeri sono pari

def conta_minimi_storici_pari(st_list):
    return conta_minimi_storici(st_list,0)

def conta_minimi_storici_dispari(st_list):
    return conta_minimi_storici(st_list,1)


# FINE area entro la quale ti richiediamo/consigliamo di operare.
    
n, p = map(int, input().strip().split())
st_list = list(map(int, input().strip().split()))
assert len(st_list) == n >= 1
assert 0 <= p <= 1
if p == 0:
    print(conta_minimi_storici_pari(st_list))
else:
    print(conta_minimi_storici_dispari(st_list))
    

