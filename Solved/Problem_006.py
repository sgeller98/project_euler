# Project Euler Problem 6

def squareSums(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * i

    return sum


def nSumSquared(n):
    return pow(sum(range(1, n+1)), 2)

print(nSumSquared(100) - squareSums(100))
