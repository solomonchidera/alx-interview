#!/usr/bin/python3
"""
Module Name: making_change

Description:
    This module provides a solution to the coin change problem using dynamic programming.
    It determines the minimum number of coins needed to make a given amount from a set of coin denominations.

Contents:
    - makeChange(coins, total): Function to solve the coin change problem

Usage:
    from making_change import makeChange
    
    coins = [1, 2, 5]
    total = 11
    result = makeChange(coins, total)
    print(result)  # Output: 3 (5 + 5 + 1)

Dependencies:
    No external dependencies

Author:
    solomon //always like it in lowercase

Version:
    1.0

Date:
    2024-07-22

License:
    MIT License
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
    coins (list): A list of coin denominations available.
    total (int): The target amount to be reached.

    Returns:
    int: The fewest number of coins needed to meet the total.
         Returns 0 if total is 0 or less.
         Returns -1 if the total cannot be met by any number of coins.

    Time complexity: O(total * len(coins))
    Space complexity: O(total)
    """
    if total <= 0:
        return 0

    # Initialize dp array with total + 1 (impossible value) for all amounts
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
