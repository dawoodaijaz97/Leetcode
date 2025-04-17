MOD = 10**9 + 7

def solve(complexity: list[int]) -> int:
    n = len(complexity)
    dp = [0] * n
    dp[0] = 1
    
    # Sort indices by complexity
    sorted_indices = sorted(range(n), key=lambda x: (complexity[x], x))
    
    for i in range(1, n):
        for j in range(i):
            if complexity[sorted_indices[j]] < complexity[sorted_indices[i]]:
                dp[sorted_indices[i]] = (dp[sorted_indices[i]] + dp[sorted_indices[j]]) % MOD
    
    # Sum up all valid permutations starting with 0
    return sum(dp) % MOD