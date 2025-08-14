def solve(n: int, costs: list[int]) -> int:
    """
    Calculate the minimum total cost to reach step n from step 0.

    :param n: Number of steps (1-indexed)
    :param costs: List of costs for each step (1-indexed)
    :return: Minimum total cost to reach step n
    """
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(i + 1, min(i + 4, n + 1)):
            dp[j] = min(dp[j], dp[i] + costs[j - 1] + (j - i) ** 2)

    return dp[n]