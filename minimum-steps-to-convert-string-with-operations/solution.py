def solve(word1: str, word2: str) -> int:
    n = len(word1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                replace = dp[i - 1][j - 1] + 1
                delete = dp[i - 1][j] + 1
                insert = dp[i][j - 1] + 1
                dp[i][j] = min(replace, delete, insert)
    
    return dp[n][n]