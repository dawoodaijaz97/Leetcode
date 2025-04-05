from typing import List

def solve(nums: List[int], k: int) -> List[int]:
    def is_valid_permutation(perm):
        concatenated_value = int(''.join(map(str, perm)))
        return concatenated_value % k == 0

    nums.sort()
    n = len(nums)
    
    for i in range(n):
        if nums[i] % k == 0:
            continue
        for j in range(i + 1, n):
            if (nums[i] * 10 + nums[j]) % k == 0:
                nums[i], nums[j] = nums[j], nums[i]
                return nums
    
    for perm in permutations(nums):
        if is_valid_permutation(perm):
            return list(perm)
    
    return []

from itertools import permutations