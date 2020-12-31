# Project Euler Problem 39

def is_triplet(a, b, c, p):
    if a + b + c != p:
        return False
    if pow(a, 2) + pow(b, 2) != pow(c, 2):
        return False

    return True


def len_triplets(n):
    numTriples = 0
    for a in range(1, n):
        for b in range(a, n):
            if is_triplet(a, b, n - a - b, n):
                print(a, b, n-a-b)
                numTriples += 1

    return numTriples


def findLongestTriplet(limit):
    maxperimeter = 120
    for n in range(120, limit+1):
        if len_triplets(n) > len_triplets(maxperimeter):
            maxperimeter = n
        else:
            pass

    return maxperimeter

print(findLongestTriplet(1000))
