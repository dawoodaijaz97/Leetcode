from typing import List, Tuple
import heapq

def solve(grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0)]  # right, down
    pq: List[Tuple[int, int, int, int]] = [(grid[0][0], 0, 0, k)]
    visited = set()
    
    while pq:
        cost, x, y, teleports = heapq.heappop(pq)
        
        if (x, y, teleports) in visited:
            continue
        visited.add((x, y, teleports))
        
        if x == m - 1 and y == n - 1:
            return cost
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                heapq.heappush(pq, (cost + grid[nx][ny], nx, ny, teleports))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= grid[x][y]:
                    if teleports > 0 and (i, j, teleports - 1) not in visited:
                        heapq.heappush(pq, (cost, i, j, teleports - 1))
    
    return -1