# -*- coding: utf-8 -*-
# Soluzione di conta_multipli, written by Romeo Rizzi 2018.12.05

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def gcd(a, b): # returns the greatest common divisor of a and b
    assert a >= 0 and b >= 0 
    while a != b and a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a > 0:
        return a
    else:
        return b

def mcm(a, b): # returns the minimum common multiple of a and b
    assert a >= 0 and b >= 0
    return (a*b)//gcd(a, b)
    
def conta_multipli(a, b, c):
    divisible_by_a = c//a
    divisible_by_both_a_and_b = c//mcm(a,b)
    return divisible_by_a - divisible_by_both_a_and_b
    
a, b, c = map(int, input().strip().split())
print(conta_multipli(a, b, c))

