"""
* user:  VR437151
* fname: GIACOMO
* lname: BARTOLI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:32:48.793382
"""
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
    n = 0
    for i in range(0, len(p)):
        for j in range(0,len(p)):
            if i <j and p[i] > p[j]:
                n = n+1
    return(n)

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
