from typing import List

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(nums: List[int]) -> int:
    n = len(nums)
    primes = {i for i, x in enumerate(nums) if is_prime(x)}
    
    from collections import deque
    
    queue = deque([(0, 0)])  # (current_index, steps)
    visited = set([0])
    
    while queue:
        current_index, steps = queue.popleft()
        
        if current_index == n - 1:
            return steps
        
        for next_index in [current_index + 1, current_index - 1]:
            if 0 <= next_index < n and next_index not in visited:
                visited.add(next_index)
                queue.append((next_index, steps + 1))
        
        if current_index in primes:
            for i in range(n):
                if i != current_index and nums[i] % nums[current_index] == 0 and i not in visited:
                    visited.add(i)
                    queue.append((i, steps + 1))
    
    return -1