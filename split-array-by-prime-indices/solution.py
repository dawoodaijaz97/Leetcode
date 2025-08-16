def is_prime(n: int) -> bool:
    """Check if a number is prime."""
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

def solve(nums: list[int]) -> int:
    """Return the absolute difference between the sums of elements at prime indices and other indices."""
    sum_prime_indices = 0
    sum_other_indices = 0
    
    for index, value in enumerate(nums):
        if is_prime(index):
            sum_prime_indices += value
        else:
            sum_other_indices += value
    
    return abs(sum_prime_indices - sum_other_indices)