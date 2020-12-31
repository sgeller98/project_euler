# Project Euler Problem 4


def ispalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


lst = []
for i in range(999):
    for j in range(999)[::-1]:
        if(ispalindrome(i * j)):
            lst.append(i * j)

print(max(lst))
