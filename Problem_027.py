# Project Euler Problem 27

import numpy as np

def eqn(a, b, n):
    return n**2 + a * n + b

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

max_ab = (1, 1)

for a in range(1, 1000):
    for b in range(1, 1000):
        
