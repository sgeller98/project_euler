# Project Euler Problem 42

"""
t(n) = (n * (n+1))/2
2 * t(n) = n* (n+1)
"""

from string import ascii_uppercase

letterToNum = {v: k for k, v in dict(enumerate(ascii_uppercase, 1)).items()}
# triangleNums = {n: int((n * (n+1))/2) for n in range(1, 1000)}
triangleNums = set([int((n * (n+1))/2) for n in range(1,1000)])

names = [name[1:-1] for name in open('p042_words.txt', 'r').read().split(",")]

def getNameScore(name):
    return sum([letterToNum[letter] for letter in name])

total = 0
for index, name in enumerate(names, start=1):
    if(getNameScore(name) in triangleNums):
        total += 1

print(total)
