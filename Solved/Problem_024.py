# Project Euler Problem 24

import itertools

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = list(itertools.permutations(nums))

print(perms[1000000-1])
