"""
* user:  VR437605
* fname: ANNALISA
* lname: DETTORI
* task:  game2stacks
* score: 0.0
* date:  2018-12-05 12:59:04.566461
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from __future__ import print_function
import sys


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

input
