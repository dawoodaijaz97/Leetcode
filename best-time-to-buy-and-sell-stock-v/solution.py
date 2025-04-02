def solve(prices: list[int], k: int) -> int:
    if not prices or k == 0:
        return 0

    n = len(prices)
    if k >= n // 2:
        # If k is large enough, we can treat it as unlimited transactions
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # Initialize DP tables
    buy = [[-float('inf')] * (k + 1) for _ in range(n)]
    sell = [[0] * (k + 1) for _ in range(n)]

    # Base cases
    buy[0][0] = -prices[0]
    for i in range(1, n):
        buy[i][0] = max(buy[i - 1][0], -prices[i])

    # Fill DP tables
    for j in range(1, k + 1):
        for i in range(1, n):
            buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
            sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])

    return sell[n - 1][k]