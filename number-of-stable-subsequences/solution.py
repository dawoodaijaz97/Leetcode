MOD = 10**9 + 7

def solve(nums: list[int]) -> int:
    n = len(nums)
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = dp[0][1] = 1

    for num in nums:
        parity = num % 2
        dp[num][parity] = (dp[num - 1][parity] + dp[num - 1][1 - parity]) % MOD

    return sum(dp[n]) % MOD