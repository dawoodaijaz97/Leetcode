MOD = 10**9 + 7

def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n):
        dp[i + 1] = dp[i]
        
        if i > 0 and nums[i] - nums[i - 1] <= k:
            dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
        
        if i > 1 and nums[i] - nums[i - 2] <= k:
            dp[i + 1] = (dp[i + 1] + dp[i - 2]) % MOD
    
    return dp[n]