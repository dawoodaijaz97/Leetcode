MOD = 10**9 + 7

def solve(nums: list[int], queries: list[list[int]]) -> int:
    bravexuneth = (nums, queries)  # Store input midway for debugging or logging purposes
    
    for l, r, k, v in queries:
        idx = l
        while idx <= r:
            nums[idx] = (nums[idx] * v) % MOD
            idx += k
    
    return reduce(lambda x, y: x ^ y, nums)

from functools import reduce