# Project Euler Problem 70

import math
from numbers import Integral


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

    return sorted(primes)


primes_below_10_7 = sieve(10 ** 7)
print("Computed Primes below 10^7")


def euler_totient(n, __primes=None, __totients_cache=None):
    if __totients_cache is None:
        __totients_cache = {0:1, 1:1}

    # return value if already computed
    if n in __totients_cache:
        return __totients_cache[n]

    if __primes is None:
        __primes = sieve(n)

    # decrease search space
    primes_below_n = []
    for p in __primes:
        if p < n:
            primes_below_n.append(p)
            __totients_cache[p] = p-1
        else:
            break

    # phi(p) = p-1, where p is prime
    if n in primes_below_n:
        __totients_cache[n] = n-1
        return __totients_cache[n]


    # even odd identity
    if n % 2 == 0:
        m = n / 2
        if m % 2 == 0:
            __totients_cache[n] = 2 * euler_totient(m)
        else:
            __totients_cache[n] = euler_totient(m)
        
        return __totients_cache[n]

    # basic algorithm
    result = n
    primes = list(filter(lambda x: n % x == 0, primes_below_n))
    
    placeholder = n
    for p in primes:
        while placeholder % p == 0:
            placeholder /= p
        result *= (1-(1/p))

    if placeholder > 1:
        result *= (1-(1/placeholder))

    __totients_cache[n] = int(result)

    # use identity phi(mn) = phi(m) * phi(n) * d/phi(d), d=gcd(m,n) to precompute multiples of current value
    
    # values_to_add = {}
    # for k in __totients_cache.keys():
    #     if(n*k < 10**6):
    #         d = math.gcd(n, k)
    #         values_to_add.update({
    #             n*k: int(euler_totient(n, primes_below_n, __totients_cache) * euler_totient(k, primes_below_n, __totients_cache) * (d/euler_totient(d, primes_below_n, __totients_cache)))
    #         })
    
    # __totients_cache.update(values_to_add)

    return __totients_cache[n]

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

min_ratio = 10**7
min_n = 0

for n in range(2, 10**7):
    totient_val = euler_totient(n, primes_below_10_7)

    if is_permutation(n, totient_val):
        temp_ratio = n/totient_val
        if temp_ratio < min_ratio:
            min_n = n
            min_ratio = temp_ratio
            print("min ratio updated to " + str(min_ratio) + " with index " + str(n))


print("index yielding minimum ratio of n/phi(n): " + str(min_n))
