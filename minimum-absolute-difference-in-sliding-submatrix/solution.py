from typing import List

def solve(grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    result = [[0] * (n - k + 1) for _ in range(m - k + 1)]
    
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            submatrix = [grid[x][y] for x in range(i, i + k) for y in range(j, j + k)]
            submatrix.sort()
            min_diff = float('inf')
            for a, b in zip(submatrix, submatrix[1:]):
                min_diff = min(min_diff, abs(a - b))
            result[i][j] = min_diff
    
    return result