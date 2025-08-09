from functools import lru_cache

def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    
    @lru_cache(None)
    def xor_up_to(i: int) -> int:
        return nums[i] ^ (xor_up_to(i - 1) if i > 0 else 0)
    
    @lru_cache(None)
    def min_max_xor(start: int, subarrays_left: int) -> int:
        if subarrays_left == 1:
            return xor_up_to(n - 1) ^ xor_up_to(start - 1) if start > 0 else xor_up_to(n - 1)
        
        max_xor = float('inf')
        for end in range(start, n - subarrays_left + 2):
            current_xor = xor_up_to(end - 1) ^ (xor_up_to(start - 1) if start > 0 else 0)
            max_xor = min(max_xor, max(current_xor, min_max_xor(end, subarrays_left - 1)))
        
        return max_xor
    
    return min_max_xor(0, k)