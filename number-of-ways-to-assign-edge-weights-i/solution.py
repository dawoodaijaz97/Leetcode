MOD = 10**9 + 7

def solve(edges: list[list[int]]) -> int:
    from collections import defaultdict, deque
    
    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find the maximum depth and nodes at that depth
    def bfs_for_depth():
        queue = deque([(1, 0)])  # (node, depth)
        max_depth = 0
        nodes_at_max_depth = []
        
        while queue:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
                nodes_at_max_depth = [node]
            elif depth == max_depth:
                nodes_at_max_depth.append(node)
            
            for neighbor in graph[node]:
                if neighbor != 1:  # Avoid revisiting the root
                    queue.append((neighbor, depth + 1))
        
        return max_depth, nodes_at_max_depth
    
    max_depth, nodes_at_max_depth = bfs_for_depth()
    
    # Count the number of ways to make the path cost odd
    def count_ways_to_odd_cost(node: int) -> int:
        queue = deque([(node, 0)])  # (node, current_path_weight)
        ways = 0
        
        while queue:
            node, current_path_weight = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor != node:  # Avoid revisiting the parent
                    new_weight = current_path_weight ^ 1  # Toggle between 0 and 1
                    if new_weight == 1:  # We want an odd cost path
                        ways += 1
                        ways %= MOD
                    queue.append((neighbor, new_weight))
        
        return ways
    
    total_ways = 0
    for node in nodes_at_max_depth:
        total_ways += count_ways_to_odd_cost(node)
        total_ways %= MOD
    
    return total_ways