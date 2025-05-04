from typing import List, Tuple

def solve(n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    from collections import defaultdict
    from functools import lru_cache
    
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v, w in edges:
        tree[u].append((v, w))
        tree[v].append((u, w))
    
    # LCA (Lowest Common Ancestor) using Binary Lifting
    MAX_LOG = 20
    parent = [[-1] * MAX_LOG for _ in range(n)]
    depth = [0] * n
    
    def dfs(node: int, par: int, d: int) -> None:
        parent[node][0] = par
        depth[node] = d
        for nei, _ in tree[node]:
            if nei != par:
                dfs(nei, node, d + 1)
    
    dfs(0, -1, 0)
    
    for k in range(MAX_LOG - 1):
        for i in range(n):
            if parent[i][k] != -1:
                parent[i][k + 1] = parent[parent[i][k]][k]
    
    def lca(u: int, v: int) -> int:
        if depth[u] > depth[v]:
            u, v = v, u
        for k in range(MAX_LOG):
            if (depth[v] - depth[u]) & (1 << k):
                v = parent[v][k]
        if u == v:
            return u
        for k in range(MAX_LOG - 1, -1, -1):
            if parent[u][k] != parent[v][k]:
                u = parent[u][k]
                v = parent[v][k]
        return parent[u][0]
    
    # Weighted median calculation
    def weighted_median(u: int, v: int) -> int:
        l = lca(u, v)
        total_weight = 0
        
        @lru_cache(None)
        def dfs_weight(node: int, par: int) -> Tuple[int, List[Tuple[int, int]]]:
            nonlocal total_weight
            weight_sum = 0
            path_weights = []
            for nei, w in tree[node]:
                if nei != par:
                    sub_weight, sub_path = dfs_weight(nei, node)
                    weight_sum += sub_weight
                    path_weights.extend(sub_path)
            weight_sum += sum(w for _, w in tree[node] if w > 0 and _ != par)
            total_weight += weight_sum
            path_weights.append((node, weight_sum))
            return weight_sum, path_weights
        
        dfs_weight(u, -1)
        dfs_weight(v, -1)
        dfs_weight(l, -1)
        dfs_weight(parent[l][0], -1) if parent[l][0] != -1 else None
        
        half_weight = total_weight // 2
        current_weight = 0
        for node, weight in sorted(path_weights, key=lambda x: depth[x[0]]):
            current_weight += weight
            if current_weight >= half_weight:
                return node
    
    # Process each query
    result = []
    for u, v in queries:
        result.append(weighted_median(u, v))
    
    return result