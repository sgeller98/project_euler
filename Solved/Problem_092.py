# Project Euler Problem 92

def digit_square_sum(n):
    return sum(map(lambda x: x ** 2, map(int, str(n))))


ends_in_1 = {1, 10, 13, 32, 44}
ends_in_89 = {89, 58, 37, 16, 4, 20, 42, 145}
total = 0
for n in range(1, 10000000+1):
    i = n
    while(True):
        if i == 1 or i in ends_in_1:
            ends_in_1.add(n)
            break
        elif i == 89 or i in ends_in_89:
            ends_in_89.add(n)
            total += 1
            break
        else:
            i = digit_square_sum(i)

print(total)
