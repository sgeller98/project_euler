# Project Euler Problem 34

from scipy.special import factorial


def is_digitFactorialSum(n):
    return sum([factorial(int(dig)) for dig in str(n)]) == n


print(sum(filter(is_digitFactorialSum, range(3, 1854721))))
