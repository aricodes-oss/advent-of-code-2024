#!/usr/bin/env python

a: list[int] = []
b: list[int] = []

with open("input", "r") as f:
    for line in f:
        lhs, rhs = [int(val) for val in line.rstrip().split()]
        a.append(lhs)
        b.append(rhs)


distances: list[int] = []
for lhs, rhs in zip(sorted(a), sorted(b)):
    distances.append(abs(lhs - rhs))

print(sum(distances))
