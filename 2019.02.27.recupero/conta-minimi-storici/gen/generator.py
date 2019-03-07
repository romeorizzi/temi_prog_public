#!/usr/bin/env python3

import random
import argparse

from limits import *

parser = argparse.ArgumentParser()
parser.add_argument("N", type=int, help="numero di elementi della lista")
parser.add_argument("P", type=int, choices=(0, 1), help="0 = minimi storici pari, 1 = minimi storici dispari")
parser.add_argument("E", type=int, choices=(0, 1, 2), help="0 = valori sia pari che dispari, 1 = solo pari, 2 = solo dispari")
parser.add_argument("seed", type=int, help="seed per il generatore random")
args = parser.parse_args()

random.seed(args.seed)
assert 0 <= args.N <= MAXN 

if args.E == 0: # genera valori sia pari che dispari
    vals = [random.randrange(0, MAXV, 1) for _ in range(args.N)]
if args.E == 1: # genera valori solo pari
    vals = [random.randrange(0, MAXV, 2) for _ in range(args.N)]
if args.E == 2: # genera valori solo dispari
    vals = [random.randrange(1, MAXV, 2) for _ in range(args.N)]

print(args.N, args.P)
print(" ".join(str(v) for v in vals))
