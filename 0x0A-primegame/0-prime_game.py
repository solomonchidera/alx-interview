#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def listPrime(n):
    """A function that generates a list of primes."""
    numbers = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            numbers.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return numbers


def isWinner(x, nums):
    """A function that determines the winner of the prime games."""
    ben_score = maria_score = 0
    for num in nums[:x]:
        turn = 0
        for pick in listPrime(num):
            turn = 1 - turn
        if turn:
            maria_score += 1
        else:
            ben_score += 1
    if maria_score > ben_score:
        return "Maria"
    elif maria_score < ben_score:
        return "Ben"
    else:
        return None
