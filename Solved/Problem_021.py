# Project Euler Problem 21


def properDivisors(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


def d(n):
    return sum(properDivisors(n))


amicableN = 0

for i in range(1, 10000+1):
    a = d(i)
    b = d(a)
    if i == b and i != a:
        amicableN += a

print(amicableN)
