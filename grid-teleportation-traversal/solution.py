from collections import deque, defaultdict

def solve(matrix: list[str]) -> int:
    m, n = len(matrix), len(matrix[0])
    portals = defaultdict(list)
    
    # Collect portal positions
    for i in range(m):
        for j in range(n):
            if matrix[i][j].isalpha():
                portals[matrix[i][j]].append((i, j))
    
    # BFS setup
    queue = deque([(0, 0, 0, set())])  # (row, col, moves, used_portals)
    visited = set()
    visited.add((0, 0, frozenset()))
    
    while queue:
        i, j, moves, used_portals = queue.popleft()
        
        if i == m - 1 and j == n - 1:
            return moves
        
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] != '#':
                new_portals = used_portals.copy()
                if matrix[i][j].isalpha() and matrix[i][j] not in new_portals:
                    for portal_pos in portals[matrix[i][j]]:
                        if (portal_pos[0], portal_pos[1]) != (i, j):
                            queue.append((portal_pos[0], portal_pos[1], moves + 1, new_portals | {matrix[i][j]}))
                else:
                    queue.append((ni, nj, moves + 1, new_portals))
    
    return -1