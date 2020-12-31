# Project Euler Problem 25


def digitLen(n):
    return len(str(n))


def fib(n):
    def fibCalc(num):
        if num == 0:
            return (0, 1)
        else:
            a, b = fibCalc(num // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if num % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return fibCalc(n)[0]


n = 1
while True:
    if digitLen(fib(n)) == 1000:
        print(n)
        break
    else:
        n += 1
