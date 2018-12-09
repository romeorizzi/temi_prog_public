"""
* user:  VR437605
* fname: ANNALISA
* lname: DETTORI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 13:08:02.969300
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input č raw_input


n1 = int(input())
n2 = int(input())

def play(n1,n2):  # questa č la funzione che devi perfezionare
    togli1=0
    togli2=0
    if (n1>n2):
        togli1=n1-n2
    if (n2>n1):
        togli2=n2-n1
    return (togli1, togli2)    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

