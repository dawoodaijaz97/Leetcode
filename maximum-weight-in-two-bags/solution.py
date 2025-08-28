from typing import List

def solve(weights: List[int], max_capacity1: int, max_capacity2: int) -> int:
    """
    Find the maximum total weight that can be placed in two bags
    with given capacities.
    
    Args:
        weights: List of item weights
        max_capacity1: Maximum capacity of first bag
        max_capacity2: Maximum capacity of second bag
        
    Returns:
        Maximum possible total weight in both bags
    """
    # Dynamic programming approach for 0/1 knapsack
    def knapsack(capacity: int, items: List[int]) -> List[int]:
        dp = [0] * (capacity + 1)
        for weight in items:
            for w in range(capacity, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + weight)
        return dp
    
    # Solve for both bags
    bag1_weights = knapsack(max_capacity1, weights)
    bag2_weights = knapsack(max_capacity2, weights)
    
    # Find maximum combined weight
    max_weight = 0
    for i in range(len(bag1_weights)):
        for j in range(len(bag2_weights)):
            if i + j <= max_capacity1 + max_capacity2:
                max_weight = max(max_weight, bag1_weights[i] + bag2_weights[j])
    
    return max_weight