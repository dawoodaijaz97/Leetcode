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

def solve(nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    prime_count = [0] * n
    distinct_primes = set()
    
    for i, num in enumerate(nums):
        if is_prime(num):
            distinct_primes.add(num)
            prime_count[i] = len(distinct_primes)
    
    prefix_prime_count = [0] * (n + 1)
    suffix_prime_count = [0] * (n + 1)
    
    for i in range(n):
        prefix_prime_count[i + 1] = prefix_prime_count[i] + prime_count[i]
    
    for i in range(n - 1, -1, -1):
        suffix_prime_count[i] = suffix_prime_count[i + 1] + prime_count[i]
    
    result = []
    
    for idx, val in queries:
        if is_prime(nums[idx]):
            distinct_primes.discard(nums[idx])
        
        nums[idx] = val
        
        if is_prime(val):
            distinct_primes.add(val)
        
        max_distinct_primes = 0
        for k in range(1, n + 1):
            left_primes = prefix_prime_count[k]
            right_primes = suffix_prime_count[k]
            if nums[idx] in distinct_primes:
                left_primes -= 1
            if idx < k and nums[idx] in distinct_primes:
                right_primes += 1
            max_distinct_primes = max(max_distinct_primes, left_primes + right_primes)
        
        result.append(max_distinct_primes)
    
    return result