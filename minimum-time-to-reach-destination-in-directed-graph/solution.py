from typing import List, Tuple
import heapq

def solve(n: int, edges: List[List[int]]) -> int:
    # Create adjacency list with time constraints
    adj_list = [[] for _ in range(n)]
    for u, v, start, end in edges:
        adj_list[u].append((v, start, end))
    
    # Priority queue to store (time, node)
    pq: List[Tuple[int, int]] = [(0, 0)]
    # Set to keep track of visited nodes with the minimum time
    visited = [float('inf')] * n
    
    while pq:
        current_time, current_node = heapq.heappop(pq)
        
        if current_node == n - 1:
            return current_time
        
        if current_time >= visited[current_node]:
            continue
        
        visited[current_node] = current_time
        
        for neighbor, start, end in adj_list[current_node]:
            # Calculate the next possible time to use the edge
            wait_time = max(start, current_time + 1)
            if wait_time <= end:
                heapq.heappush(pq, (wait_time + (end - wait_time), neighbor))
    
    return -1