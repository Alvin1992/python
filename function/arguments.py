#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: arguments.py


def powersum(power, *args):
    """Return the sum of each argument raised to specified power."""
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print powersum(2, 3, 4)
print powersum(2, 10)
