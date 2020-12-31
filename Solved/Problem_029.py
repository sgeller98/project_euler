# Project Euler Problem 29


def powerCombosLen(bottom, limit):
    combos = set()

    for a in range(bottom, limit+1):
        for b in range(bottom, limit+1):
            p = pow(a, b)
            if p not in combos:
                combos.add(p)

    return len(combos)

# print(powerCombosLen(2, 5)) Works

print(powerCombosLen(2, 100))
