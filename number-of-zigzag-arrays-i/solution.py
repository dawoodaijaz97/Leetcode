MOD = 10**9 + 7

def solve(n: int, l: int, r: int) -> int:
    if n < 3 or l >= r:
        return 0
    
    # dp[i][j] will store the number of valid ZigZag arrays of length i ending with j
    dp = [[0] * (r - l + 1) for _ in range(n)]
    
    # Initialize the first element of each array
    for j in range(l, r + 1):
        dp[0][j - l] = 1
    
    # Fill the DP table
    for i in range(1, n):
        for j in range(l, r + 1):
            for k in range(l, r + 1):
                if j != k:
                    dp[i][j - l] += dp[i - 1][k - l]
                    dp[i][j - l] %= MOD
    
    # Sum up all valid arrays of length n
    result = sum(dp[n - 1]) % MOD
    
    return result