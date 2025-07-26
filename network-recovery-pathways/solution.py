from typing import List

def solve(edges: List[List[int]], online: List[bool], k: int) -> int:
    from collections import defaultdict, deque
    from heapq import heappush, heappop
    
    n = len(online)
    graph = defaultdict(list)
    
    for u, v, cost in edges:
        if online[u] and online[v]:
            graph[u].append((v, cost))
    
    def dijkstra():
        pq = [(-float('inf'), 0)]
        dist = [-float('inf')] * n
        dist[0] = float('inf')
        
        while pq:
            min_cost, node = heappop(pq)
            min_cost = -min_cost
            
            if node == n - 1:
                return min_cost
            
            for neighbor, cost in graph[node]:
                new_min_cost = max(min_cost, cost)
                if new_min_cost > dist[neighbor] and new_min_cost <= k:
                    dist[neighbor] = new_min_cost
                    heappush(pq, (-new_min_cost, neighbor))
        
        return -1
    
    return dijkstra()