from typing import List
import math

def solve(nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    
    # Find the maximum value in nums to limit our GCD calculations
    max_val = max(nums)
    
    # dp[i][j] will store the number of increasing subsequences ending with nums[j] and having GCD i
    dp = [[0] * (n + 1) for _ in range(max_val + 1)]
    
    # Initialize dp for single element subsequences
    for j in range(n):
        dp[nums[j]][j + 1] = 1
    
    # Fill the dp table
    for i in range(1, max_val + 1):
        for j in range(1, n + 1):
            if dp[i][j] == 0:
                continue
            for k in range(j + 1, n + 1):
                if nums[k - 1] > nums[j - 1]:
                    new_gcd = math.gcd(i, nums[k - 1])
                    dp[new_gcd][k] = (dp[new_gcd][k] + dp[i][j]) % MOD
    
    # Calculate the total beauty
    total_beauty = 0
    for i in range(1, max_val + 1):
        count = sum(dp[i]) % MOD
        total_beauty = (total_beauty + i * count) % MOD
    
    return total_beauty

# Example usage:
# solve([1, 2, 3])
# solve([4, 6])