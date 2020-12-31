# Project Euler Problem 14


def collatzLen(n, l):
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1

        l += 1
    return l


index = 0
lm = 0
for n in range(2, 1000000):
    l0 = collatzLen(n, 0)
    if l0 > lm:
        lm = l0
        index = n

print(index)
