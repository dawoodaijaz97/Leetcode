MOD = 10**9 + 7

def solve(n: int, l: int, r: int) -> int:
    if n == 3:
        return (r - l + 1) * (r - l) % MOD
    
    # dp[i][j] will store the number of valid ZigZag arrays of length i ending with j
    dp = [[0] * (r - l + 1) for _ in range(3)]
    
    # Initialize for arrays of length 2
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            dp[2][j - l] += 1
        for j in range(i - 1, l - 1, -1):
            dp[2][j - l] += 1
    
    # Fill the dp table for arrays of length 3 to n
    for i in range(4, n + 1):
        new_dp = [[0] * (r - l + 1) for _ in range(3)]
        for j in range(l, r + 1):
            for k in range(j + 1, r + 1):
                new_dp[i % 3][k - l] += dp[(i - 2) % 3][j - l]
                new_dp[i % 3][k - l] %= MOD
            for k in range(j - 1, l - 1, -1):
                new_dp[i % 3][k - l] += dp[(i - 2) % 3][j - l]
                new_dp[i % 3][k - l] %= MOD
        dp = new_dp
    
    # Sum up all valid arrays of length n
    result = sum(dp[n % 3]) % MOD
    return result