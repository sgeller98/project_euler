# Project Euler Problem 5


def divisibleBy10(n):
    for i in [5, 6, 7, 8, 9, 10]:
        if n % i != 0:
            return False

    return True


def divisibleBy20(n):
    for i in [11, 13, 14, 16, 17, 18, 19, 20]:
        if n % i != 0:
            return False

    return True


i = 2520
while True:
    if divisibleBy20(i):
        print(i)
        break
    else:
        i += 2520
