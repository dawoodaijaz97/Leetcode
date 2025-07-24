from typing import List

MOD = 10**9 + 7

def solve(edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    from collections import defaultdict, deque
    
    n = len(edges) + 1
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def lca(u: int, v: int) -> int:
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        
        def dfs(node: int, par: int, d: int):
            parent[node] = par
            depth[node] = d
            for nei in graph[node]:
                if nei != par:
                    dfs(nei, node, d + 1)
        
        dfs(1, 0, 0)
        
        if depth[u] > depth[v]:
            u, v = v, u
        
        while depth[v] > depth[u]:
            v = parent[v]
        
        while u != v:
            u = parent[u]
            v = parent[v]
        
        return u
    
    def count_odd_paths(u: int, v: int) -> int:
        l = lca(u, v)
        path_length = (depth[u] + depth[v] - 2 * depth[l]) % 2
        if path_length == 0:
            return 0
        else:
            return pow(2, (depth[u] + depth[v] - 2 * depth[l]) // 2, MOD)
    
    result = []
    for u, v in queries:
        result.append(count_odd_paths(u, v))
    
    return result