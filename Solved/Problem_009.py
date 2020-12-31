# Project Euler Problem 9


def tripletFind(limit):
    triplets = []
    for x in range(1, limit):
        xx = x * x
        y = x + 1
        z = y + 1

        while (z <= limit):
            zz = xx + (y * y)
            while(z * z < zz):
                z += 1
            if z * z == zz and z <= limit:
                triplets.append((x, y, z))
            y += 1

    return triplets

for triplet in tripletFind(1000):
    if sum(triplet) == 1000:
        print(triplet[0] * triplet[1] * triplet[2])
