# Project Euler Problem 35

from itertools import permutations
import math


def sieve(limit):
    primes = []
    multiples = set()
    for i in range(2, limit+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, limit+1, i))

    return primes


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def list_is_prime(nums):
    return all(map(is_prime, nums))


def rotate(s):
    s = str(s)
    return [int(s[n:] + s[:n]) for n in range(len(s))]


def getCircularPrimes(limit):
    nums = []
    for n in sieve(limit):
        if list_is_prime(rotate(n)):
            nums.append(n)

    return nums

print(len(getCircularPrimes(1000000)))
