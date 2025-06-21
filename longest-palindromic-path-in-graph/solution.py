from typing import List

def solve(n: int, edges: List[List[int]], label: str) -> int:
    from collections import defaultdict
    
    # Build adjacency list for the graph
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    def dfs(node: int, path: List[int], visited: set) -> int:
        max_length = 0
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [label[neighbor]]
                if is_palindrome(new_path):
                    max_length = max(max_length, len(new_path))
                max_length = max(max_length, dfs(neighbor, new_path, visited))
                visited.remove(neighbor)
        return max_length
    
    max_palindrome_length = 0
    for start_node in range(n):
        visited = {start_node}
        path = [label[start_node]]
        max_palindrome_length = max(max_palindrome_length, dfs(start_node, path, visited))
    
    return max_palindrome_length