from collections import defaultdict

def solve(arrivals: list[int], w: int, m: int) -> int:
    """
    Calculate the minimum number of arrivals to discard so that every w-day window contains at most m occurrences of each type.
    
    :param arrivals: List of item types arriving on each day.
    :param w: The size of the sliding window.
    :param m: The maximum allowed occurrences of any item type within the window.
    :return: Minimum number of discards required.
    """
    item_count = defaultdict(int)
    discard_count = 0
    
    for i, item in enumerate(arrivals):
        item_count[item] += 1
        
        if i >= w:
            leftmost_item = arrivals[i - w]
            item_count[leftmost_item] -= 1
            if item_count[leftmost_item] == 0:
                del item_count[leftmost_item]
        
        if item_count[item] > m:
            discard_count += 1
            item_count[item] -= 1
    
    return discard_count