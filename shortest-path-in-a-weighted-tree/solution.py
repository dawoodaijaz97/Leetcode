from typing import List, Tuple

def solve(n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    from collections import defaultdict
    from heapq import heappop, heappush
    
    # Build the graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Dijkstra's algorithm to find shortest path from root to all nodes
    def dijkstra(start: int) -> List[int]:
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heappop(priority_queue)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(priority_queue, (distance, neighbor))
        
        return distances
    
    # Initial shortest path from root to all nodes
    shortest_paths = dijkstra(1)
    
    # Process queries
    answers = []
    for query in queries:
        if query[0] == 1:  # Update edge weight
            u, v, w_prime = query[1], query[2], query[3]
            # Find the index of the edge to update
            for i, (edge_u, edge_v, _) in enumerate(edges):
                if (u, v) == (edge_u, edge_v) or (v, u) == (edge_u, edge_v):
                    edges[i][2] = w_prime
                    break
            # Recalculate shortest paths from root after update
            shortest_paths = dijkstra(1)
        elif query[0] == 2:  # Query shortest path to node x
            x = query[1]
            answers.append(shortest_paths[x])
    
    return answers