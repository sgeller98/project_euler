# Project Euler Problem 10


def sieve(limit):
    primes = []
    multiples = set()
    for i in range(2, limit+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, limit+1, i))

    return primes

below2m = sieve(2000000)

print(sum(below2m))
