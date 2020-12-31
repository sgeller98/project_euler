# Project Euler Problem 41

import functools
import itertools
import math


def sieve(limit):
    primes = []
    multiples = set()
    for i in range(2, limit + 1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i * i, limit + 1, i))

    return primes


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gen_permutations(n=7654321):
    return [int(''.join(x)) for x in itertools.permutations(str(n)) if len(str(int(''.join(x)))) == len(str(n))]

print(max([x for x in gen_permutations() if is_prime(x)]))
