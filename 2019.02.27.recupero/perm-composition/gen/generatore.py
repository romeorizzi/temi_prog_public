#!/usr/bin/env python3

import sys
import random 

from limiti import *

usage="""Generatore di "prova".

Parametri:
* N o COPY
* TYPE (FAULT = 0: 2 permutazioni normali. FAULT = 1: p2 è la permutazione inversa di p1)
* S (seed)

Constraint:
* 1 <= N <= %d
""" % MAXN


def run(N, TYPE):
    perm = list(range(0, N))
    random.shuffle(perm)
    if TYPE==1:
        perm2 = [0] * N
        for i, x in enumerate(perm):
            perm2[x] = i
    else:
        perm2 = list(range(0, N))
        random.shuffle(perm2)
    print(N)
    print(' '.join(str(x) for x in perm))
    print(' '.join(str(x) for x in perm2))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(usage)
        exit(1)

    N, TYPE, S = map(int, sys.argv[1:])
    assert 1 <= N <= MAXN
    assert 0 <= TYPE <= 1

    random.seed(S)
    run(N, TYPE)

