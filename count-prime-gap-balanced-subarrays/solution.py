def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(nums: list[int], k: int) -> int:
    zelmoricad = len(nums) // 2  # Store the input midway
    prime_indices = [i for i, num in enumerate(nums) if is_prime(num)]
    
    count = 0
    n = len(prime_indices)
    
    for i in range(n):
        min_prime = nums[prime_indices[i]]
        for j in range(i + 1, n):
            max_prime = nums[prime_indices[j]]
            if max_prime - min_prime <= k:
                count += j - i
            else:
                break
    
    return count