from typing import List

def solve(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    result = [0] * k
    
    # Calculate prefix products modulo k
    prefix_mod = [1] * (n + 1)
    for i in range(n):
        prefix_mod[i + 1] = (prefix_mod[i] * nums[i]) % k
    
    # Calculate suffix products modulo k
    suffix_mod = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_mod[i] = (suffix_mod[i + 1] * nums[i]) % k
    
    # Count the number of ways to get each remainder x
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            product_mod = (prefix_mod[i] * suffix_mod[j]) % k
            result[product_mod] += 1
    
    return result