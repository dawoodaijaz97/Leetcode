from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    
    # Calculate prefix sums
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
    
    # Find the maximum sum of increasing subarrays ending at each index
    max_increasing_sum_ending_at = [0] * n
    current_max = float('-inf')
    for i in range(n):
        if i == 0 or nums[i] > nums[i - 1]:
            current_max = max(current_max, prefix_sums[i + 1])
        max_increasing_sum_ending_at[i] = current_max
    
    # Find the maximum sum of decreasing subarrays starting at each index
    max_decreasing_sum_starting_at = [0] * n
    current_max = float('-inf')
    for i in range(n - 1, -1, -1):
        if i == n - 1 or nums[i] > nums[i + 1]:
            current_max = max(current_max, prefix_sums[n] - prefix_sums[i])
        max_decreasing_sum_starting_at[i] = current_max
    
    # Find the maximum sum of trionic subarrays
    max_trionic_sum = float('-inf')
    for q in range(2, n - 1):
        if nums[q - 1] > nums[q] < nums[q + 1]:
            left_sum = max_increasing_sum_ending_at[q - 1]
            right_sum = max_decreasing_sum_starting_at[q + 1]
            trionic_sum = prefix_sums[q + 2] - prefix_sums[q - 1] + left_sum + right_sum
            max_trionic_sum = max(max_trionic_sum, trionic_sum)
    
    return max_trionic_sum