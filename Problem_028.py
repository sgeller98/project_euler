# Project Euler Problem 28

import numpy as np


def ulam_corner(k, n):
    if np.mod(n, 4) == 1:
        return np.pow((2 * k + 1), 2)
    elif np.mod(n, 4) == 3:
        return 4 * np.pow(k, 2) + 1
    else:
        return np.pow(k, 2) + k + 1

print([ulam_corner(k, n) for ])
