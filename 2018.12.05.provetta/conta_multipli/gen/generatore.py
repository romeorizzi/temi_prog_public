#!/usr/bin/env python3
import sys
import random

assert len(sys.argv) > 2

if sys.argv[1] == "COPY":
    with open(sys.argv[2]) as f:
        print(f.read())
    exit(0)

assert len(sys.argv) == 4

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

assert 1 <= a <= 10**100
assert 1 <= b <= 10**100
assert 1 <= c <= 10**100

print(a, b, c)

