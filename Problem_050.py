# Project Euler Problem 50

def sieve(limit):
    primes = []
    multiples = set()
    for i in range(2, limit+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, limit+1, i))

    return primes

primes_below_million = sieve(1000000)

def longest_consecutive_prime_sum(n):
    primes_below_n = sorted(p for p in primes_below_million if p < n)
    
    max_length = 0
    prime_with_max_length = 2

    for start in range(len(primes_below_n)):
        for end in range(start+max_length, len(primes_below_n)):
            cur_sum = sum(primes_below_n[start:end])
            if cur_sum in primes_below_n:
                cur_length = end-start
                if cur_length > max_length:
                    max_length = cur_length
                    prime_with_max_length = cur_sum
                else:
                    pass
            else:
                pass

    return prime_with_max_length

print(longest_consecutive_prime_sum(1000))

