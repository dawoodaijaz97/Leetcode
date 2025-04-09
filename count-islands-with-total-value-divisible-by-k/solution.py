from typing import List

def solve(grid: List[List[int]], k: int) -> int:
    def dfs(x: int, y: int) -> int:
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        value = grid[x][y]
        grid[x][y] = 0  # Mark as visited
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            value += dfs(x + dx, y + dy)
        return value

    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:
                island_value = dfs(i, j)
                if island_value % k == 0:
                    island_count += 1

    return island_count