from typing import List

def find(parent: List[int], i: int) -> int:
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent: List[int], rank: List[int], x: int, y: int) -> None:
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def solve(n: int, edges: List[List[int]], k: int) -> int:
    if k >= n:
        return 0
    
    # Sort edges by time in descending order
    edges.sort(key=lambda x: -x[2])
    
    parent = list(range(n))
    rank = [0] * n
    components = n
    
    for u, v, time in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            components -= 1
            if components <= k:
                return time
    
    return -1  # This line should never be reached given the problem constraints

# Example usage:
# solve(2, [[0,1,3]], 2) should return 3
# solve(3, [[0,1,2],[1,2,4]], 3) should return 4
# solve(3, [[0,2,5]], 2) should return 0