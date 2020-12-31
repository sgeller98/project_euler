# Project Euler Problem 43

import functools
import itertools


def is_pandigital(num):
    return functools.reduce(lambda a, b: a+b, sorted(str(num))) == '0123456789'


def is_substring_divisible(n):
    subs = map(int, [str(n)[x:x+3] for x in range(1, len(str(n))+1)][0:-3])
    primes = [2, 3, 5, 7, 11, 13, 17]
    return all([x % y == 0 for x, y in zip(subs, primes)])

# print(is_substring_divisible(1406357289))  Working Test


def gen_permutations(n=9876543210):
    return [int(''.join(x)) for x in itertools.permutations(str(n)) if len(str(int(''.join(x)))) == len(str(n))]

print(sum([x for x in gen_permutations() if is_substring_divisible(x)]))
