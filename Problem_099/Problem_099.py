# Project Euler Problem 99

from math import exp, log
import numpy as np

with open("p099_base_exp.txt", 'r') as t:
    nums = t.readlines()
    nums = [line.split(',') for line in nums]
    nums = [[int(l[0]), int(l[1])] for l in nums]
    nums = [l[0] ** l[1] for l in nums]

