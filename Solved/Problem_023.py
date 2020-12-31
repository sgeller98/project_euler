# Project Euler Problem 23

limit = 20162  # Wolfram Alpha Limit
total = 0
abundantNums = set()


def d(n):
    def properDivisors(num):
        for i in range(1, num):
            if num % i == 0:
                yield i
    return sum(properDivisors(n))

for n in range(1, limit):
    if d(n) > n:
        abundantNums.add(n)
    if not any((n-a in abundantNums) for a in abundantNums):
        total += n

print(total)
