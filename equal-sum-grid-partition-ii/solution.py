from typing import List

def solve(grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    
    # Calculate prefix sums for rows and columns
    row_prefix_sums = [[0] * (n + 1) for _ in range(m)]
    col_prefix_sums = [[0] * (m + 1) for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            row_prefix_sums[i][j + 1] = row_prefix_sums[i][j] + grid[i][j]
            col_prefix_sums[j][i + 1] = col_prefix_sums[j][i] + grid[i][j]
    
    # Check horizontal cuts
    for i in range(1, m):
        top_sum = row_prefix_sums[i - 1][-1]
        bottom_sum = row_prefix_sums[-1][-1] - top_sum
        
        if top_sum == bottom_sum:
            return True
        
        # Try discounting one cell from the top or bottom
        for j in range(n):
            if top_sum + grid[i - 1][j] == bottom_sum or bottom_sum + grid[i - 1][j] == top_sum:
                return True
    
    # Check vertical cuts
    for j in range(1, n):
        left_sum = col_prefix_sums[j - 1][-1]
        right_sum = col_prefix_sums[-1][-1] - left_sum
        
        if left_sum == right_sum:
            return True
        
        # Try discounting one cell from the left or right
        for i in range(m):
            if left_sum + grid[i][j - 1] == right_sum or right_sum + grid[i][j - 1] == left_sum:
                return True
    
    return False