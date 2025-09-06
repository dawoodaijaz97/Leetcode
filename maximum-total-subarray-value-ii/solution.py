from typing import List

def solve(nums: List[int], k: int) -> int:
    n = len(nums)
    max_values = [0] * n
    min_values = [0] * n
    
    # Calculate max and min values for subarrays ending at each index
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            max_values[i] = nums[stack[-1]]
        else:
            max_values[i] = nums[i]
        stack.append(i)
    
    stack.clear()
    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            min_values[i] = nums[stack[-1]]
        else:
            min_values[i] = nums[i]
        stack.append(i)
    
    # Calculate the maximum total value
    max_heap = []
    for i in range(n):
        for j in range(i, n):
            subarray_value = max_values[j] - min_values[i]
            if len(max_heap) < k:
                import heapq
                heapq.heappush(max_heap, subarray_value)
            elif subarray_value > max_heap[0]:
                heapq.heapreplace(max_heap, subarray_value)
    
    return sum(max_heap)

# Example usage:
# solve([1, 3, 2], 2) should return 4
# solve([4, 2, 5, 1], 3) should return 12