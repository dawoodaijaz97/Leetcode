from typing import List, Tuple

def solve(edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    from collections import defaultdict
    from heapq import heappush, heappop
    
    n = len(edges) + 1
    graph = defaultdict(list)
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dijkstra(start: int) -> List[int]:
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                alt = d + w
                if alt < dist[v]:
                    dist[v] = alt
                    heappush(pq, (alt, v))
        
        return dist
    
    def find_lca(u: int, v: int) -> int:
        nonlocal depth
        
        if depth[u] > depth[v]:
            u, v = v, u
        
        diff = depth[v] - depth[u]
        for _ in range(diff):
            v = parent[v]
        
        while u != v:
            u = parent[u]
            v = parent[v]
        
        return u
    
    def dfs(u: int, p: int) -> None:
        nonlocal depth
        parent[u] = p
        depth[u] = depth[p] + 1
        
        for v, _ in graph[u]:
            if v != p:
                dfs(v, u)
    
    parent = [0] * n
    depth = [0] * n
    
    dfs(0, -1)
    
    def calculate_subtree_weight(src1: int, src2: int, dest: int) -> int:
        lca = find_lca(src1, src2)
        
        dist_src1 = dijkstra(src1)
        dist_src2 = dijkstra(src2)
        dist_dest = dijkstra(dest)
        
        min_weight = float('inf')
        
        for u in range(n):
            if depth[u] >= depth[lca]:
                weight = (dist_src1[u] + dist_src2[u] + dist_dest[u]) - 2 * dist_dest[lca]
                min_weight = min(min_weight, weight)
        
        return min_weight
    
    result = []
    for src1, src2, dest in queries:
        result.append(calculate_subtree_weight(src1, src2, dest))
    
    return result