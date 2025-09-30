from typing import List

def solve(nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)
    for k in range(len(queries) + 1):
        current_nums = nums[:]
        for i in range(k):
            l, r, val = queries[i]
            for j in range(l, r + 1):
                current_nums[j] -= val
        if all(x == 0 for x in current_nums):
            return k
    return -1