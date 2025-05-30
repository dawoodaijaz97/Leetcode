from typing import List, Dict

def solve(x: List[int], y: List[int]) -> int:
    # Dictionary to store the top 3 largest y values for each unique x value
    max_y_values: Dict[int, List[int]] = {}
    
    for xi, yi in zip(x, y):
        if xi not in max_y_values:
            max_y_values[xi] = []
        # Insert yi into the sorted list of top 3 y values for this x
        from bisect import insort
        insort(max_y_values[xi], yi)
        if len(max_y_values[xi]) > 3:
            max_y_values[xi].pop(0)
    
    # Find the maximum sum of y values from three distinct x values
    max_sum = -1
    for xi, yi in zip(x, y):
        # Get the top 2 y values for this x (excluding yi itself)
        top_ys = max_y_values[xi][:-1]
        if len(top_ys) == 2:
            current_sum = yi + sum(top_ys)
            max_sum = max(max_sum, current_sum)
    
    return max_sum