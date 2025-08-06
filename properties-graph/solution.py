from typing import List, Set

def intersect(a: List[int], b: List[int]) -> int:
    return len(set(a) & set(b))

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

def solve(properties: List[List[int]], k: int) -> int:
    n = len(properties)
    parent = list(range(n))
    rank = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if intersect(properties[i], properties[j]) >= k:
                union(parent, rank, i, j)
    
    components = set(find(parent, i) for i in range(n))
    return len(components)