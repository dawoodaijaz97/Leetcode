from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return -1
    
    # Find the longest increasing subsequence (LIS) ending at each index
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Find the longest decreasing subsequence (LDS) starting at each index
    lds = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    # Find the minimum absolute difference between sums of left and right subarrays
    min_diff = float('inf')
    total_sum = sum(nums)
    
    for i in range(n-1):
        if lis[i] > 1 and lds[i+1] > 1:
            left_sum = sum(nums[j] for j in range(i+1) if lis[j] == lis[i])
            right_sum = sum(nums[j] for j in range(i+1, n) if lds[j] == lds[i+1])
            min_diff = min(min_diff, abs(left_sum - right_sum))
    
    return min_diff if min_diff != float('inf') else -1