# Project Euler Problem 22

from string import ascii_uppercase

letterToNum = {v: k for k, v in dict(enumerate(ascii_uppercase, 1)).items()}

names = [name[1:-1] for name in open('p022_names.txt', 'r').read().split(",")]

names.sort()

# print(names[938-1]) Returns Colin, the 938th name according to PE


def getScore(name):
    return sum([letterToNum[letter] for letter in name])

# print(getScore(names[938-1]) * 938)

total = 0
for index, name in enumerate(names, start=1):
    total += getScore(name) * index

print(total)
