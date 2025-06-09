def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculate the maximum sum of edge values in a graph.

    :param n: Number of nodes in the graph.
    :param edges: List of edges where each edge is represented as [a_i, b_i].
    :return: Maximum score achievable by assigning unique values to nodes.
    """
    # Sort edges based on the product of potential maximum values
    sorted_edges = sorted(edges, key=lambda e: (n - max(e), n - min(e)), reverse=True)
    
    # Initialize node values with 1
    node_values = [0] * n
    
    # Assign values to nodes
    for u, v in sorted_edges:
        if not node_values[u]:
            node_values[u] = n
            n -= 1
        if not node_values[v]:
            node_values[v] = n
            n -= 1
    
    # Calculate the maximum sum of edge values
    max_sum = sum(node_values[u] * node_values[v] for u, v in edges)
    
    return max_sum