#!/usr/bin/env python2

from limiti import *
from sys import argv, exit, stderr
import os
from numpy.random import random, randint, seed as nseed
from random import choice, sample, shuffle, seed as rseed

usage="""Generatore di "prova".

Parametri:
* N
* FAULT (FAULT = 0: una permutazione. FAULT = 1: codominio errato. FAULT = 2: non biunivoca.)
* S (seed)

Constraint:
* 1 <= N <= %d
""" % MAXN


def run(N, FAULT):
    perm = range(0,N)
    shuffle(perm)
    if FAULT==1:
        perm[randint(N)] = N + randint(2)
    if FAULT==2:
        i = randint(N)
        j = randint(N)
        assert N >= 2
        while j==i:
            j = randint(N)
        perm[i] = perm[j]
    print N
    print ' '.join(str(x) for x in perm)


if __name__ == "__main__":
    if len(argv) != 4:
        print usage
        exit(1)

    N, FAULT, S = map(int, argv[1:])
    assert (1 <= N <= MAXN)
    assert (0 <= FAULT <= 2)

    nseed(S)
    rseed(S)
    run(N, FAULT)

