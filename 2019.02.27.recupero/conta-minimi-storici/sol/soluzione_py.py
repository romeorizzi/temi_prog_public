#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Soluzione di conta_minimi_storici

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def conta_minimi_storici(st_list, p):
    if st_list[0] %2 == p:
        counter = 1
    else:
        counter = 0
    min_so_far = st_list[0]
    for dato in st_list:
        if dato < min_so_far:
            min_so_far = dato
            if dato %2 == p:
                counter = counter +1
    return counter

def conta_minimi_storici_pari(st_list):
    return conta_minimi_storici(st_list, 0)

def conta_minimi_storici_dispari(st_list):
    return conta_minimi_storici(st_list, 1)

    
n, p = map(int, input().strip().split())
st_list = list(map(int, input().strip().split()))
assert len(st_list) == n >= 1
assert 0 <= p <= 2
if p  == 0:
    print(conta_minimi_storici_pari(st_list))
else:
    print(conta_minimi_storici_dispari(st_list))
    

