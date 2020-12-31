# Project Euler Problem 26

from fractions import gcd


def sieve(limit):
    primes = []
    multiples = set()
    for i in range(2, limit+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, limit+1, i))

    return primes

for d in sieve(1000)[::-1]:
    period = 1
    while pow(10, period, d) != 1:
        period += 1
    if d-1 == period:
        break

print(d)
