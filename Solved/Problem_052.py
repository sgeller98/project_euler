# Project Euler Problem 52

def same_digit_multiple_23456(n):
    return same_digits(n, 2 * n, 3 * n, 4 * n, 5 * n, 6 * n)

def same_digits(*arg):
    a = sorted(str(arg[0]))
    for ar in arg:
        if sorted(str(ar)) != a:
            return False

    return True

n = 2
while(not same_digit_multiple_23456(n)):
    n += 1

print(n)
