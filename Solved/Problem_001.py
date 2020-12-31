#Project Euler Problem 1

import numpy as np

nums = [x for x in np.arange(1000) if x % 3 == 0 or x % 5 == 0]

print(nums)

print(sum(nums))
