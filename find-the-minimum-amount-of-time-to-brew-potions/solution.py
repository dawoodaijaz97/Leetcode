def solve(skill: list[int], mana: list[int]) -> int:
    n, m = len(skill), len(mana)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for j in range(1, m + 1):
        dp[1][j] = sum(skill[i] * mana[j - 1] for i in range(n))
    
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i - 1][k] + skill[i - 1] * mana[j - 1] for k in range(j))
    
    return dp[n][m]