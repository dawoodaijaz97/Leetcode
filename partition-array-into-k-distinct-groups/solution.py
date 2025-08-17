from collections import Counter
from typing import List

def solve(nums: List[int], k: int) -> bool:
    if len(nums) % k != 0:
        return False
    
    count = Counter(nums)
    
    for freq in count.values():
        if freq % k != 0:
            return False
    
    return True