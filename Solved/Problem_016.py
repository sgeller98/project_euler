# Project Euler Problem 16


def digitSum(n):
    return sum([int(x) for x in str(n)])

print(digitSum(pow(2, 1000)))
