from typing import List

def solve(nums: List[int], target: int) -> bool:
    def dfs(index: int, current_product: int) -> bool:
        if index == len(nums):
            return current_product == target
        
        # Include the current number in the subset
        if dfs(index + 1, current_product * nums[index]):
            return True
        
        # Exclude the current number from the subset
        if dfs(index + 1, current_product):
            return True
        
        return False
    
    # Start DFS with the first element included and excluded
    return dfs(0, 1) or dfs(0, nums[0])

# Example usage:
# solve([3, 1, 6, 8, 4], 24) should return True
# solve([2, 5, 3, 7], 15) should return False