def solve(grid: list[list[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    
    # Calculate prefix sums for rows
    row_prefix_sums = [0] * m
    for i in range(m):
        row_prefix_sums[i] = sum(grid[i])
    
    # Calculate total sum of the grid
    total_sum = sum(row_prefix_sums)
    
    # Check for horizontal cuts
    seen_row_sums = set()
    for i in range(m - 1):
        current_row_sum = row_prefix_sums[i]
        if current_row_sum * 2 == total_sum:
            return True
        seen_row_sums.add(current_row_sum)
    
    # Calculate prefix sums for columns
    col_prefix_sums = [0] * n
    for j in range(n):
        for i in range(m):
            col_prefix_sums[j] += grid[i][j]
    
    # Check for vertical cuts
    total_col_sum = sum(col_prefix_sums)
    seen_col_sums = set()
    for j in range(n - 1):
        current_col_sum = col_prefix_sums[j]
        if current_col_sum * 2 == total_col_sum:
            return True
        seen_col_sums.add(current_col_sum)
    
    return False