#!/usr/bin/env python

a: list[int] = []
b: list[int] = []

with open("input", "r") as f:
    for line in f:
        lhs, rhs = [int(val) for val in line.rstrip().split()]
        a.append(lhs)
        b.append(rhs)

# This would be much quicker using a collections.Counter,
# but for a one-off execution we don't care about timing
print(sum([el * b.count(el) for el in a]))
