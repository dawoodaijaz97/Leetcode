from typing import List

def solve(value: List[int], limit: List[int]) -> int:
    n = len(value)
    # Pair each value with its corresponding limit and sort by value in descending order
    pairs = sorted(zip(value, limit), reverse=True)
    
    total_value = 0
    active_count = 0
    
    for v, l in pairs:
        if active_count < l:
            total_value += v
            active_count += 1
    
    return total_value