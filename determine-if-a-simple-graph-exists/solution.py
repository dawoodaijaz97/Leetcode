from typing import List, Dict, Set

def solve(edges: List[List[int]], n: int) -> bool:
    """
    Determine if a simple graph exists with given edges and vertices.
    
    Args:
        edges: List of edges where each edge is [u, v]
        n: Number of vertices in the graph
        
    Returns:
        True if a valid simple graph can be formed, False otherwise
    """
    # Check for invalid edges
    if not edges:
        return True
    
    # Check if all vertices are within valid range
    max_vertex = max(max(edge) for edge in edges)
    min_vertex = min(min(edge) for edge in edges)
    
    if max_vertex >= n or min_vertex < 0:
        return False
    
    # Check for self-loops and duplicate edges
    seen_edges = set()
    for u, v in edges:
        # Self-loop check
        if u == v:
            return False
        
        # Normalize edge representation to avoid duplicates like [1,2] and [2,1]
        normalized_edge = (min(u, v), max(u, v))
        if normalized_edge in seen_edges:
            return False
        seen_edges.add(normalized_edge)
    
    return True