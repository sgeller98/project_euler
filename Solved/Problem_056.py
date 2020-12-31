# Project Euler Problem 56

def digit_sum(n):
    return sum(map(int, str(n)))

maxdigitsum = 0
for a in range(1, 100 + 1):
    for b in range(1, 100 + 1):
        cur = digit_sum(a ** b)
        if cur > maxdigitsum:
            maxdigitsum = cur

print(maxdigitsum)
