from typing import List

def solve(n: int, edges: List[List[int]], k: int) -> int:
    # Sort edges by weight in descending order
    edges.sort(key=lambda x: -x[2])
    
    # Union-Find data structure
    parent = list(range(n))
    rank = [1] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
    
    # Initialize the number of components to n (each node is its own component)
    components = n
    max_cost = 0
    
    # Iterate over edges from largest to smallest weight
    for u, v, w in edges:
        if components > k:
            # Union the nodes if they are not already connected
            if find(u) != find(v):
                union(u, v)
                components -= 1
                max_cost = w
    
    return max_cost