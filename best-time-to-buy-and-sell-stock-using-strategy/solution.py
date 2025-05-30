def solve(prices: list[int], strategy: list[int], k: int) -> int:
    n = len(prices)
    max_profit = 0

    # Calculate the original profit without any modification
    original_profit = sum(p * s for p, s in zip(prices, strategy))
    max_profit = original_profit

    # Iterate over all possible starting points of the k-length subarray
    for i in range(n - k + 1):
        # Calculate the potential new profit if we modify the subarray [i:i+k]
        modified_profit = (
            original_profit
            + sum(prices[j] for j in range(i, i + k // 2))  # Buy at these points
            - sum(prices[j] for j in range(i + k // 2, i + k))  # Sell at these points
        )
        max_profit = max(max_profit, modified_profit)

    return max_profit