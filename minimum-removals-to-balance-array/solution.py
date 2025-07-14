def solve(nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    min_removals = float('inf')
    
    for i in range(n):
        left, right = 0, i
        while left <= right:
            mid = (left + right) // 2
            if nums[i] <= nums[mid] * k:
                right = mid - 1
            else:
                left = mid + 1
        
        min_removals = min(min_removals, n - (i - left + 1))
    
    return min_removals