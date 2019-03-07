#!/usr/bin/env python3

import sys 

from limits import *

with open(sys.argv[1]) as f:
    N, P = map(int, f.readline().split())
    l = list(map(int, f.readline().split()))

assert P in (0, 1)
assert 0 <= N <= MAXN
assert len(l) == N

for v in l:
    assert 0 <= v <= MAXV