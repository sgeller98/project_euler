# Project Euler Problem 27

import numpy as np
import math

def eqn(a, b, n):
    return n**2 + a * n + b

def is_prime(n):
    if n < 0:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print("Starting calculation...")

max_len = 0
max_product = 0
max_a = 0
max_b = 0
for a in range(-1000+1, 1000): # |a| < 1000
    for b in range(-1000, 1000+1): # |b| <= 1000
        print(f"Testing ({a}, {b})")
        n = 0
        running = True
        while running:
            f = n*n + a*n + b
            if(is_prime(f)):
                if(n > max_len):
                    max_len = n
                    max_a = a
                    max_b = b
                    max_product = a*b
                
                n += 1
            else:
                running = False

print(f"Maximum length: {max_len}")
print(f"Maximum coefficients: {max_a}, {max_b}")
print(f"Maximum Coefficient Product: {max_product}")

