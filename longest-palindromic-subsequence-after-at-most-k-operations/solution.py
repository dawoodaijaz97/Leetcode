def solve(s: str, k: int) -> int:
    n = len(s)
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

    def cost(c1: str, c2: str) -> int:
        return min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2)))

    for i in range(n):
        dp[i][i][0] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for ops in range(k + 1):
                if s[i] == s[j]:
                    dp[i][j][ops] = max(dp[i][j][ops], dp[i + 1][j - 1][ops] + 2)
                if ops > 0:
                    dp[i][j][ops] = max(dp[i][j][ops], dp[i + 1][j][ops - cost(s[i], 'a')] + 1)
                    dp[i][j][ops] = max(dp[i][j][ops], dp[i][j - 1][ops - cost('z', s[j])] + 1)

    return dp[0][n - 1][k]