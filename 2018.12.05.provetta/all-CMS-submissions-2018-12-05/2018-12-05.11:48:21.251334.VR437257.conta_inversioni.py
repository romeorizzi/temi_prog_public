"""
* user:  VR437257
* fname: BENEDETTA
* lname: TOMMASI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 11:48:21.251334
"""
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input 

def numero_di_inversioni(p):
    n=0
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            if p[i]>p[j]:
                n=n+1
    return n


p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
