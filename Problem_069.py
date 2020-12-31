# Project Euler Problem 69

import math
from numbers import Integral
import time
import matplotlib.pyplot as plt


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

    result = n
    primes = list(filter(lambda x: n % x == 0, primes_below_n))

    # basic algorithm
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

max_ratio = 1.0
max_n = 1

# for n in range(2, 10):
#     totient_val = euler_totient(n)
#     temp_ratio = n/totient_val

#     if is_permutation(n, totient_val):
#         # temp_ratio = n/totient_val
#         if max_ratio < temp_ratio:
#             max_n = n
#             max_ratio = temp_ratio
#             print("max ratio updated to " + str(max_ratio) + " with index " + str(max_n))
    
#     print("n=" + str(n) + " phi(n)=" + str(totient_val) + " n/phi(n)=" + str(temp_ratio))


xs = []
ys = []

for n in range(1,10**4):
    xs.append(n)
    startTime = time.clock()
    euler_totient(n)
    endTime = time.clock()
    ys.append(endTime-startTime)

plt.plot(xs, ys, '.')
plt.show()

# print("index yielding minimum ratio of n/phi(n): " + str(max_n))
