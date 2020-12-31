# Project Euler Problem 94

import math

def triangle_area(a, b, c):
    return math.sqrt(4 * a**2 * b**2 - (a**2 + b**2 - c**2)**2)/4

total = 0
for a in range(1, 1000000000):
    areahigh = triangle_area(a, a, a+1)
    arealow = triangle_area(a, a, a-1)
    if areahigh == int(areahigh):
        total += 3*a + 1
    
    if arealow == int(arealow):
        total += 3*a - 1
