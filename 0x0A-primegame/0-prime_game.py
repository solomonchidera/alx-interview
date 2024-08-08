#!/usr/bin/python3


def isWinner(x, nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_primes(n):
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    maria_wins = 0
    for n in nums:
        if count_primes(n) % 2 == 1:
            maria_wins += 1

    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None
