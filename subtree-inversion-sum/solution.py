from typing import List, Tuple

def solve(edges: List[List[int]], nums: List[int], k: int) -> int:
    from collections import defaultdict
    from functools import lru_cache
    
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    @lru_cache(None)
    def dfs(node: int, parent: int, depth: int) -> Tuple[int, int]:
        # Calculate the sum of the subtree without inversion
        normal_sum = nums[node]
        inverted_sum = -nums[node]
        
        for child in tree[node]:
            if child == parent:
                continue
            
            child_normal, child_inverted = dfs(child, node, depth + 1)
            
            # If we invert this node, the child cannot be inverted
            normal_sum += max(child_normal, child_inverted)
            
            # If we don't invert this node, check if we can invert the child
            if depth - k >= 0:
                inverted_sum += child_normal
        
        return normal_sum, inverted_sum
    
    # Start DFS from the root node (0) with no parent and depth 0
    total_normal, total_inverted = dfs(0, -1, 0)
    
    # Return the maximum possible sum
    return max(total_normal, total_inverted)