#!/usr/bin/env python2

from limiti import *
from sys import argv, exit, stderr
import os
from numpy.random import random, randint, seed as nseed
from random import choice, sample, shuffle, seed as rseed

usage="""Generatore di "prova".

Parametri:
* N
* TYPE (= 0: permutazione casuale. = 1: p ordinata in modo decrescente, = 2: p ordine crescente)
* S (seed)

Constraint:
* 1 <= N <= %d
""" % MAXN


def run(N, TYPE):
    perm = [randint(1, 100000) for x in range(0, N)]

    if TYPE!=0:
        perm.sort()
    if TYPE==1:
        perm = list(reversed(perm))

    print(' '.join(str(x) for x in perm))

if __name__ == "__main__":
    if not(len(argv) == 4 or len(argv) == 3 and argv[1] == "COPY"):
        print(usage)
        exit(1)

    if argv[1] == "COPY":
        with open(argv[2]) as f:
            print(f.read())
        exit(0)

    N, TYPE, S = map(int, argv[1:])
    assert 1 <= N <= MAXN
    assert 0 <= TYPE <= 2

    nseed(S)
    rseed(S)
    run(N, TYPE)
