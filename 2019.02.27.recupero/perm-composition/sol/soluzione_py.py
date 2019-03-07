#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Soluzione di perm_composition, written by Alessandro Righi 2018.11.29

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

##########################################################

def perm_composition(p1, p2):
    return [
        p2[i]
        for i in p1
    ]

#########################################################

N = int(input())
p1 = list(map(int, input().strip().split()))
p2 = list(map(int, input().strip().split()))
assert len(p1) == N
assert len(p2) == N
print(*perm_composition(p1, p2))

