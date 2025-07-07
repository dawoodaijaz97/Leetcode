from typing import List

def solve(m: int, n: int, waitCost: List[List[int]]) -> int:
    # Initialize DP table with infinity
    dp = [[[float('inf')] * 2 for _ in range(n)] for _ in range(m)]
    
    # Starting point
    dp[0][0][0] = (0 + 1) * (0 + 1)
    
    # Fill the DP table
    for i in range(m):
        for j in range(n):
            if i > 0:
                # Move down from (i-1, j)
                dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][1] + (i + 1) * (j + 1))
                dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][0] + waitCost[i][j])
            if j > 0:
                # Move right from (i, j-1)
                dp[i][j][0] = min(dp[i][j][0], dp[i][j-1][1] + (i + 1) * (j + 1))
                dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][0] + waitCost[i][j])
    
    # The answer is the minimum cost to reach (m-1, n-1) on an odd-numbered second
    return dp[m-1][n-1][0]