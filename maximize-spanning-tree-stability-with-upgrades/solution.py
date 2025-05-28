from typing import List, Tuple

def solve(n: int, edges: List[List[int]], k: int) -> int:
    def find(parent: List[int], i: int) -> int:
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent: List[int], rank: List[int], x: int, y: int) -> bool:
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
            return True
        return False

    # Separate edges into mandatory and optional
    mandatory_edges = []
    optional_edges = []
    for u, v, s, must in edges:
        if must == 1:
            mandatory_edges.append((s, u, v))
        else:
            optional_edges.append((s, u, v))

    # Sort edges by strength
    optional_edges.sort()

    # Initialize union-find structures
    parent = list(range(n))
    rank = [0] * n

    # Add all mandatory edges to the spanning tree
    for s, u, v in mandatory_edges:
        if not union(parent, rank, u, v):
            return -1  # Cycle detected among mandatory edges

    # Try to add optional edges while considering upgrades
    min_strength = float('inf')
    upgrade_count = k
    for s, u, v in optional_edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            min_strength = max(min_strength, s)
            if upgrade_count > 0 and s * 2 > min_strength:
                min_strength = s * 2
                upgrade_count -= 1

    # Check if all nodes are connected
    root_set = {find(parent, i) for i in range(n)}
    if len(root_set) != 1:
        return -1

    return min_strength