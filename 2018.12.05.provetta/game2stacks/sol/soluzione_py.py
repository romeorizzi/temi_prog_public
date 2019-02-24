#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# soluzione di game2stacks

#from __future__ import print_function
#import sys
#if sys.version_info < (3, 0):
#    input = raw_input # in python2, l'equivalente di input è raw_input


def play(n1, n2):
    if n1 == n2:
        return (0,0)
    if n1 > n2:
        return (n1-n2, 0)
    if n2 > n1:
        return (0, n2-n1)
    

n1 = int(input())
n2 = int(input())

togli1, togli2 = play(n1, n2)
    
print(togli1)
print(togli2)


