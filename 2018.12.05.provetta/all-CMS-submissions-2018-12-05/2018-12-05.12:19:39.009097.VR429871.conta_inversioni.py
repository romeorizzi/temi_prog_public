"""
* user:  VR429871
* fname: MARCO
* lname: GHIOTTO
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:19:39.009097
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
	l= len(p)
	a=0
	for count in range (l):
		for c in range (count+1, l):
			if p[count]>p[c]:
				a=a+1
	return a

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
