# Coin Change Problem Solution

the algorithm used to solve the coin change problem efficiently using dynamic programming.

## Algorithm Steps

1. **Initial Check**: 
   - If the total is 0 or less, return 0 as no coins are needed.

2. **Initialize DP Array**: 
   - Create a `dp` array of size `total + 1`.
   - Initialize all elements with `total + 1` (an impossible value).
   - `dp[i]` represents the minimum number of coins needed to make amount `i`.

3. **Base Case**: 
   - Set `dp[0] = 0` since it takes 0 coins to make an amount of 0.

4. **Iterate Through Amounts**: 
   - Loop through all amounts from 1 to `total`.

5. **Calculate Minimum Coins**: 
   - For each amount, try all coin denominations:
     a. If coin value <= current amount:
        - Option 1: Don't use this coin (keep previous minimum)
        - Option 2: Use this coin (add 1 to minimum coins for `amount - coin`)
     b. Take the minimum of these two options.

6. **Final Result**: 
   - After filling the `dp` array, `dp[total]` contains the minimum number of coins needed.

7. **Check Possibility**: 
   - If `dp[total]` is still `total + 1`, return -1 (impossible to make the amount).
   - Otherwise, return `dp[total]`.

## Complexity Analysis

- **Time Complexity**: O(total * len(coins))
- **Space Complexity**: O(total)
