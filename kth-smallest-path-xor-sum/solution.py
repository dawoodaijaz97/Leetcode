from typing import List, Dict

def solve(par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
    from collections import defaultdict
    
    n = len(vals)
    tree = defaultdict(list)
    
    for i in range(1, n):
        tree[par[i]].append(i)
    
    def dfs(node: int) -> List[int]:
        xor_sums = [vals[node]]
        for child in tree[node]:
            xor_sums.extend([xor ^ vals[child] for xor in dfs(child)])
        return xor_sums
    
    results = []
    for u, k in queries:
        subtree_xor_sums = dfs(u)
        unique_xor_sums = sorted(set(subtree_xor_sums))
        if k <= len(unique_xor_sums):
            results.append(unique_xor_sums[k - 1])
        else:
            results.append(-1)
    
    return results