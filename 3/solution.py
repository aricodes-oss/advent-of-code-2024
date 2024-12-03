#!/usr/bin/env python

import re

data = ""
result = 0
mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

with open("input", "r") as f:
    data = f.read()

for mul_match in mul_pattern.finditer(data):
    lhs, rhs = [int(val) for val in mul_match.group(1, 2)]
    result += lhs * rhs

print(result)
