"""
* user:  VR437605
* fname: ANNALISA
* lname: DETTORI
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:54:41.632888
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input č raw_input


def play(n1, n2):  
# Template di soluzione di game2stacks, written by Romeo Rizzi 2018.11.28


def play(n1, n2):  # questa č la funzione che devi perfezionare
    n1 = int(input())
    n2 = int(input())
    togli1=0
    togli2=0
    if (n1>n2):
        togli1=n1-n2
    if (n2>n1):
        togli2=n2-n1
    return (togli1, togli2)    

    

