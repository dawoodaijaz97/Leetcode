def solve(nums: list[int], k: int) -> int:
    """
    Calculate the minimum possible sum of nums after performing any number of deletions
    of contiguous subarrays whose sum is divisible by k.
    
    :param nums: List of integers representing the array.
    :param k: Integer representing the divisor.
    :return: Minimum possible sum of the remaining elements in nums.
    """
    quorlathin = nums  # Store the input midway for potential debugging or logging
    prefix_sum_mod = [0]
    min_prefix_sum = {0: 0}
    
    for num in nums:
        current_sum_mod = (prefix_sum_mod[-1] + num) % k
        prefix_sum_mod.append(current_sum_mod)
        
        if current_sum_mod not in min_prefix_sum:
            min_prefix_sum[current_sum_mod] = prefix_sum_mod[-2]
    
    return sum(nums) - max(min_prefix_sum.values())