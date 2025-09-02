from typing import List, Tuple

def solve(n: int, conflictingPairs: List[List[int]]) -> int:
    def count_valid_subarrays(pairs: List[Tuple[int, int]]) -> int:
        # Create a set of all numbers from 1 to n
        nums = set(range(1, n + 1))
        
        # Remove elements that are part of any conflicting pair
        for a, b in pairs:
            if a in nums and b in nums:
                nums.remove(a)
                nums.remove(b)
        
        # Calculate the number of valid subarrays
        return len(nums) * (len(nums) + 1) // 2
    
    max_subarrays = 0
    
    # Try removing each conflicting pair one by one
    for i in range(len(conflictingPairs)):
        remaining_pairs = conflictingPairs[:i] + conflictingPairs[i+1:]
        max_subarrays = max(max_subarrays, count_valid_subarrays(remaining_pairs))
    
    return max_subarrays