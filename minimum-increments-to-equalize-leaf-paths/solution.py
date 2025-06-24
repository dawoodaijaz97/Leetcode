from typing import List

def solve(n: int, edges: List[List[int]], cost: List[int]) -> int:
    from collections import defaultdict
    
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    def dfs(node: int, parent: int) -> int:
        total_cost = cost[node]
        max_child_cost = 0
        
        for neighbor in tree[node]:
            if neighbor != parent:
                child_cost = dfs(neighbor, node)
                total_cost += child_cost
                max_child_cost = max(max_child_cost, child_cost)
        
        # The number of increments needed for this node
        increments = max(0, max_child_cost - cost[node])
        return total_cost + increments
    
    # Start DFS from the root (node 0) with an initial parent of -1
    dfs(0, -1)
    
    # The result is the number of nodes that need their cost increased
    return n - 1

# Example usage:
# solve(3, [[0,1],[0,2]], [2,1,3]) should return 1
# solve(3, [[0,1],[1,2]], [5,1,4]) should return 0
# solve(5, [[0,4],[0,1],[1,2],[1,3]], [3,4,1,1,7]) should return 1