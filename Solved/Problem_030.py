# Project Euler Problem 30

limit = 5 * pow(9, 5)


def is_digitPowSum(num, p):
    return sum([pow(int(n), p) for n in str(num)]) == num


print(sum([n for n in range(10, limit) if is_digitPowSum(n, 5)]))
