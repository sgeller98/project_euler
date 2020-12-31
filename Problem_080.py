# Project Euler Problem 80

import math
import decimal

decimal.getcontext().prec = 100

def decimal_sum(n):
    return sum(map(int, str(n).split('.')[1]))


total = 0
for i in range(100+1):
    if i**2 not in range(1, 100):
        print(i)
        total += decimal_sum(decimal.Decimal(i).sqrt())

print(total)