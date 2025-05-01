MOD = 10**9 + 7

def solve(m: int, k: int, nums: list[int]) -> int:
    from itertools import combinations_with_replacement
    from functools import reduce
    from operator import mul
    
    def count_set_bits(n: int) -> int:
        return bin(n).count('1')
    
    total_sum = 0
    for seq in combinations_with_replacement(range(len(nums)), m):
        if count_set_bits(sum(1 << i for i in seq)) == k:
            product = reduce(mul, (nums[i] for i in seq), 1)
            total_sum = (total_sum + product) % MOD
    
    return total_sum