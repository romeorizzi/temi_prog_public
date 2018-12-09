"""
* user:  VR437123
* fname: ISOTTA
* lname: CARAVAGGI
* task:  conta_inversioni
* score: 100.0
* date:  2018-12-05 12:13:00.515402
"""
# -*- coding: utf-8 -*-
# Template per la soluzione del problema conta_inversioni

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input

def numero_di_inversioni(p):
	h= len(p)
	y=0
	for count in range (h):
		for x in range (count+1,h):
			if p[count]>p[x]:
				y=y+1
	return y

p = list(map(int, input().strip().split()))
print(numero_di_inversioni(p))
