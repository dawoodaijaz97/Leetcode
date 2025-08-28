def solve(nums):
    """
    Find the length of the longest semi-repeating subarray.
    
    A semi-repeating subarray is defined as a subarray where at most one 
    element appears more than once.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of longest semi-repeating subarray
    """
    if not nums:
        return 0
    
    max_length = 1
    left = 0
    count = {}
    
    for right in range(len(nums)):
        # Add current element to window
        count[nums[right]] = count.get(nums[right], 0) + 1
        
        # Shrink window until at most one duplicate exists
        while len(count) < (right - left + 1) - sum(1 for c in count.values() if c > 1):
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length