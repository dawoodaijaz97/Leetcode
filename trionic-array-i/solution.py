def solve(nums: list[int]) -> bool:
    n = len(nums)
    
    # Find the first peak (q) where nums[q] is the maximum in nums[0...n-1]
    q = max(range(1, n - 1), key=nums.__getitem__)
    
    # Check if there exists a valid p such that nums[0...p] is strictly increasing
    for p in range(q):
        if not (nums[p] < nums[p + 1]):
            return False
    
    # Check if there exists a valid r such that nums[q...r] is strictly decreasing
    for r in range(q, n - 1):
        if not (nums[r] > nums[r + 1]):
            return False
    
    return True