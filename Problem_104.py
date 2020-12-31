# Project Euler Problem 104

import functools

def fib(x):
    @functools.lru_cache(maxsize=None)
    def _fib(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = _fib(n//2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (, )
            else:
                return (d, c + d)

    return _fib(x)[0]

def is_pandigital(n):
    return functools.reduce(lambda a, b: a+b, sorted(str(n))) == '123456789'

def is_pandigital_ends(n):
    return is_pandigital(int(str(n)[:9])) and is_pandigital(int(str(n)[-9:]))

k = 2749
while True:
    # print(f"Trying k = {k}")
    if is_pandigital_ends(fib(k)):
        print(k)
        break
    else:
        k += 1


