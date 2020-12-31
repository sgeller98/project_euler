#!/usr/local/var/pyenv/shims/python3

#Project Euler Problem 2

import numpy as np

from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-2) + fib(n-1)


def fibSum(limit):
    total = 0
    x = 0
    while fib(x) < limit:
        cur = fib(x)
        if np.mod(cur, 2) == 0:
            total += cur
        x += 1

    return total

print(fibSum(4000000))
