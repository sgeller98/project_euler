# Project Euler Problem 20


def digitSum(n):
    return sum(map(int, list(str(n))))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(digitSum(factorial(100)))
