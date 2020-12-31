# Project Euler Problem 62

import itertools

def gen_permutations(n):
    return list(set([int(''.join(x)) for x in itertools.permutations(str(n)) if len(str(int(''.join(x)))) == len(str(n))]))


print(len(gen_permutations(41063625)))
