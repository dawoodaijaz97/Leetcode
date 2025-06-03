from typing import List

MOD = 10**9 + 7

def solve(vals: List[int], par: List[int]) -> int:
    from collections import defaultdict, Counter
    
    n = len(vals)
    tree = defaultdict(list)
    
    for i in range(1, n):
        tree[par[i]].append(i)
    
    def dfs(node: int) -> (int, int):
        max_score = 0
        digit_count = Counter()
        
        for child in tree[node]:
            child_score, child_digits = dfs(child)
            if all(digit_count[d] == 0 for d in child_digits):
                max_score += child_score
                digit_count.update(child_digits)
        
        current_digit_count = Counter(str(vals[node]))
        if all(digit_count[d] == 0 for d in current_digit_count):
            max_score += vals[node]
            digit_count.update(current_digit_count)
        
        return max_score, digit_count
    
    total_sum = 0
    for i in range(n):
        max_score, _ = dfs(i)
        total_sum = (total_sum + max_score) % MOD
    
    return total_sum