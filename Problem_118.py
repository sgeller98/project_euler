# Project Euler Problem 118

import math
import itertools

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def pandigitalSubsets(n):
    out = set()

