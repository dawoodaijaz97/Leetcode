from typing import List, Tuple

def solve(n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    from collections import defaultdict
    from functools import lru_cache

    # Build the tree structure
    tree = defaultdict(list)
    for u, v in hierarchy:
        tree[u].append(v)

    @lru_cache(None)
    def dfs(node: int, remaining_budget: int) -> int:
        max_profit = 0
        original_price = present[node - 1]
        discounted_prices = [floor(present[v] / 2) for v in tree[node]]

        # Option 1: Buy the stock at the original price
        if original_price <= remaining_budget:
            profit = future[node - 1] - original_price
            max_profit = max(max_profit, profit + sum(dfs(v, remaining_budget - original_price) for v in tree[node]))

        # Option 2: Buy the stock at the discounted price
        for i, v in enumerate(tree[node]):
            if discounted_prices[i] <= remaining_budget:
                profit = future[v - 1] - discounted_prices[i]
                max_profit = max(max_profit, profit + dfs(v, remaining_budget - discounted_prices[i]) + sum(dfs(w, remaining_budget) for w in tree[node] if w != v))

        return max_profit

    # Start DFS from the CEO (node 1)
    return dfs(1, budget)

# Helper function to calculate floor division
def floor(x: int, y: int) -> int:
    return x // y