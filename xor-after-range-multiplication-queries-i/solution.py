MOD = 10**9 + 7

def solve(nums: list[int], queries: list[list[int]]) -> int:
    for l, r, k, v in queries:
        idx = l
        while idx <= r:
            nums[idx] = (nums[idx] * v) % MOD
            idx += k
    
    return reduce(lambda x, y: x ^ y, nums)