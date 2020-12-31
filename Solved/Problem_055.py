# Project Euler Problem 55

def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def reverse(n):
    return int(str(n)[::-1])

def is_lychrel(n):
    for _ in range(50):
        n += reverse(n)
        if is_palindrome(n):
            return False
    return True

print(len(list(filter(is_lychrel, range(10000)))))
