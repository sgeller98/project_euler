# Project Euler Problem 45

def triangle(n):
    return int((n * (n+1))/2)

def pentagonal(n):
    return int((n * ((3*n) - 1))/2)

def hexagonal(n):
    return int(n * ((2*n) - 1))

assert(triangle(285) == pentagonal(165) and pentagonal(165) == hexagonal(143))

