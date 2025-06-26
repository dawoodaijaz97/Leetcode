def solve(nums: list[int]) -> int:
    n = len(nums)
    sorted_nums = sorted(nums)
    
    # If already sorted, return 0
    if nums == sorted_nums:
        return 0
    
    max_k = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            k = nums[i] & nums[j]
            if k > 0:
                # Check if swapping nums[i] and nums[j] helps in sorting
                nums[i], nums[j] = nums[j], nums[i]
                if nums == sorted_nums:
                    max_k = max(max_k, k)
                nums[i], nums[j] = nums[j], nums[i]  # Swap back to original
    
    return max_k