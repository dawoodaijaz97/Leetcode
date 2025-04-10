from collections import defaultdict
from typing import List

def solve(points: List[List[int]]) -> int:
    MOD = 10**9 + 7
    
    # Group points by their y-coordinate
    y_to_x = defaultdict(set)
    for x, y in points:
        y_to_x[y].add(x)
    
    # Count the number of unique horizontal trapezoids
    count = 0
    y_values = sorted(y_to_x.keys())
    
    for i in range(len(y_values)):
        for j in range(i + 1, len(y_values)):
            y1, y2 = y_values[i], y_values[j]
            x1_set = y_to_x[y1]
            x2_set = y_to_x[y2]
            
            # Find the number of ways to choose two segments from x1_set and x2_set
            count += len(x1_set) * (len(x1_set) - 1) // 2 * len(x2_set) * (len(x2_set) - 1) // 2
            count %= MOD
    
    return count