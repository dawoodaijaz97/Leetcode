from typing import List

def solve(n: int, edges: List[List[int]], score: List[int]) -> int:
    from collections import defaultdict, deque
    
    # Build the graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Initialize the queue with nodes having no incoming edges
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    
    # Topological sort using Kahn's algorithm
    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Calculate the maximum profit
    max_profit = 0
    for position, node in enumerate(topological_order, start=1):
        max_profit += score[node] * position
    
    return max_profit