def solve(fruits: list[int], baskets: list[int]) -> int:
    """
    Solve the Fruits Into Baskets III problem.

    :param fruits: List of integers representing the quantity of each type of fruit.
    :param baskets: List of integers representing the capacity of each basket.
    :return: The number of fruit types that remain unplaced after all possible allocations are made.
    """
    from collections import deque

    # Sort baskets by capacity in descending order
    baskets.sort(reverse=True)
    
    # Use a deque to efficiently pop the largest available basket
    baskets_deque = deque(baskets)
    
    # Count of unplaced fruit types
    unplaced_count = 0
    
    for fruit_quantity in fruits:
        placed = False
        while baskets_deque:
            if baskets_deque[0] >= fruit_quantity:
                baskets_deque.popleft()
                placed = True
                break
            else:
                baskets_deque.popleft()
        
        if not placed:
            unplaced_count += 1
    
    return unplaced_count