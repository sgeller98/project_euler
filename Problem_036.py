# Project Euler Problem 36


def is_binary_palindrome(n):
    n = str("{0:b}".format(n))
    return n[:int(len(n)/2)] == n[int(len(n)/2):][::-1]


def is_decimal_palindrome(n):
    n = str(n)
    if len(n) % 2:
        return n[:int(len(n)/2)+1] == n[int(len(n)/2):][::-1]
    else:
        return n[:int(len(n)/2)] == n[int(len(n)/2):][::-1]


def is_double_palindrome(n):
    return is_binary_palindrome(n) and is_decimal_palindrome(n)

# print(sum([n for n in range(1000000) if is_double_palindrome(n)]))

sum = 0
for n in range(1000000):
    if is_double_palindrome(n):
        # print(n)
        # print("{0:b}".format(n))
        sum += n

print(sum)
