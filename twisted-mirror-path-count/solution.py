MOD = 10**9 + 7

def solve(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # DP table to store the number of ways to reach each cell
    dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]
    dp[0][0][0] = 1  # Starting point
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                # Move right
                if j > 0:
                    dp[i][j][0] += dp[i][j-1][0]
                    dp[i][j][0] %= MOD
                # Move down
                if i > 0:
                    dp[i][j][1] += dp[i-1][j][1]
                    dp[i][j][1] %= MOD
            else:
                # Reflect from right to down
                if j > 0 and dp[i][j-1][0] > 0:
                    dp[i][j][1] += dp[i][j-1][0]
                    dp[i][j][1] %= MOD
                # Reflect from down to right
                if i > 0 and dp[i-1][j][1] > 0:
                    dp[i][j][0] += dp[i-1][j][1]
                    dp[i][j][0] %= MOD
    
    return (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD