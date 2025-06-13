from typing import List, Tuple

def solve(n: int, edges: List[List[int]], k: int, t: int) -> int:
    from collections import defaultdict
    from heapq import heappush, heappop
    
    # Build the graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # Priority queue to store (negative weight sum, edge count, current node)
    pq = [(-0, 0, i) for i in range(n)]
    
    # Dictionary to store the maximum weight sum for each node with a certain number of edges
    max_weight = {i: defaultdict(lambda: float('-inf')) for i in range(n)}
    max_weight[0][0] = 0
    
    while pq:
        neg_weight_sum, edge_count, node = heappop(pq)
        weight_sum = -neg_weight_sum
        
        if edge_count == k:
            continue
        
        for neighbor, weight in graph[node]:
            new_weight_sum = weight_sum + weight
            new_edge_count = edge_count + 1
            
            if new_weight_sum < t and new_weight_sum > max_weight[neighbor][new_edge_count]:
                max_weight[neighbor][new_edge_count] = new_weight_sum
                heappush(pq, (-new_weight_sum, new_edge_count, neighbor))
    
    # Find the maximum weight sum for any node with exactly k edges
    result = float('-inf')
    for i in range(n):
        if max_weight[i][k] != float('-inf'):
            result = max(result, max_weight[i][k])
    
    return result if result != float('-inf') else -1