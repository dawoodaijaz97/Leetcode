from typing import List

def solve(nums: List[int], k: int) -> int:
    n = len(nums)
    max_value = 0
    
    # Calculate the maximum value of subarrays ending at each index
    max_subarray_values = [0] * n
    current_max = nums[0]
    for i in range(n):
        current_max = max(current_max, nums[i])
        max_subarray_values[i] = current_max - min(nums[:i+1])
    
    # Calculate the maximum total value by choosing k subarrays
    total_value = 0
    for i in range(n):
        if k > 0:
            total_value += max_subarray_values[i]
            k -= 1
    
    return total_value