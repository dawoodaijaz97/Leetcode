from typing import List

def solve(nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
    def count_ways_to_get_x(nums: List[int], x: int) -> int:
        n = len(nums)
        prefix_mod = [1] * (n + 1)
        suffix_mod = [1] * (n + 1)
        
        for i in range(n):
            prefix_mod[i + 1] = (prefix_mod[i] * nums[i]) % k
        
        for i in range(n - 1, -1, -1):
            suffix_mod[i] = (suffix_mod[i + 1] * nums[i]) % k
        
        count = 0
        for i in range(n + 1):
            if (prefix_mod[i] * suffix_mod[i]) % k == x:
                count += 1
        
        return count

    result = []
    for index, value, start, x in queries:
        nums[index] = value
        modified_nums = nums[start:]
        result.append(count_ways_to_get_x(modified_nums, x))
    
    return result