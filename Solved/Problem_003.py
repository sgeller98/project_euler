# Project Euler Problem 3
import numpy as np

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sieve(limit):
    primes = []
    multiples = set()
    for i in range(2, limit+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, limit+1, i))

    return primes

def primeFactor(n):
    primes = []
    if n < 2:
        return primes
    for p in sieve(int(np.sqrt(n))):
        if p * p > n:
            break
        while n % p == 0:
            primes.append(p)
            n //= p
    if n > 1:
        primes.append(n)

    return primes

def primeFactor2(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n /= 2

    for i in range(3, int(np.floor(np.sqrt(n))), 2):
        while n % i == 0:
            primes.append(i)
            n /= i

    if n > 2:
        primes.append(n)

    return primes



print(primeFactor2(600851475143)[-1])
