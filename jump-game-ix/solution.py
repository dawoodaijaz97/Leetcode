def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = nums[:]
    
    # Forward pass
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = max(ans[stack[-1]], nums[i])
        stack.append(i)
    
    # Backward pass
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = max(ans[stack[-1]], nums[i])
        stack.append(i)
    
    return ans