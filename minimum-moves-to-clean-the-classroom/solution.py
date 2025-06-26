from typing import List, Tuple

def solve(classroom: List[str], energy: int) -> int:
    from collections import deque
    
    m, n = len(classroom), len(classroom[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < m and 0 <= y < n and classroom[x][y] != 'X'
    
    start = None
    litter_positions = []
    
    for i in range(m):
        for j in range(n):
            if classroom[i][j] == 'S':
                start = (i, j)
            elif classroom[i][j] == 'L':
                litter_positions.append((i, j))
    
    if not start or not litter_positions:
        return -1
    
    def bfs(start: Tuple[int, int], energy: int) -> int:
        queue = deque([(start, energy, 0)])
        visited = set()
        visited.add((start, energy))
        
        while queue:
            (x, y), current_energy, moves = queue.popleft()
            
            if not litter_positions:
                return moves
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    next_energy = current_energy - 1
                    if classroom[nx][ny] == 'R':
                        next_energy = energy
                    if (nx, ny, next_energy) not in visited:
                        visited.add((nx, ny, next_energy))
                        queue.append(((nx, ny), next_energy, moves + 1))
                    
                    if classroom[nx][ny] == 'L':
                        new_litter_positions = litter_positions[:]
                        new_litter_positions.remove((nx, ny))
                        bfs_result = bfs((nx, ny), next_energy)
                        if bfs_result != -1:
                            return bfs_result + moves + 1
        
        return -1
    
    return bfs(start, energy)

# code here