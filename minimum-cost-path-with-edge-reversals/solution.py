from typing import List, Tuple
import heapq

def solve(n: int, edges: List[List[int]]) -> int:
    # Create adjacency lists for original and reverse edges
    forward_edges = [[] for _ in range(n)]
    reverse_edges = [[] for _ in range(n)]
    
    for u, v, w in edges:
        forward_edges[u].append((v, w))
        reverse_edges[v].append((u, 2 * w))
    
    # Priority queue for Dijkstra's algorithm
    pq: List[Tuple[int, int, bool]] = [(0, 0, False)]  # (cost, node, switch_used)
    visited = [[float('inf'), float('inf')] for _ in range(n)]
    visited[0] = [0, 0]
    
    while pq:
        cost, node, switch_used = heapq.heappop(pq)
        
        if node == n - 1:
            return cost
        
        # Explore forward edges
        for neighbor, weight in forward_edges[node]:
            new_cost = cost + weight
            if not switch_used and visited[neighbor][0] > new_cost:
                visited[neighbor][0] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, True))
        
        # Explore reverse edges
        for neighbor, weight in reverse_edges[node]:
            new_cost = cost + weight
            if visited[neighbor][1] > new_cost:
                visited[neighbor][1] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, switch_used))
    
    return -1