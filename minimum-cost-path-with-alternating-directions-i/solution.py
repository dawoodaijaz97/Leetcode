from typing import List

def solve(grid: List[List[int]]) -> int:
    """
    Finds the minimum cost path in a grid with alternating directions.

    :param grid: A 2D list of integers representing the grid.
    :return: The minimum cost to traverse the grid.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    # Fill the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill the first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the rest of the dp table
    for i in range(1, rows):
        for j in range(1, cols):
            if (i + j) % 2 == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][cols - 1]