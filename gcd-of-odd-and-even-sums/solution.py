import math

def solve(n: int) -> int:
    """
    Compute the GCD of sum of first n odd numbers and sum of first n even numbers.
    
    Args:
        n: Number of terms
        
    Returns:
        GCD of sumOdd and sumEven
    """
    # Sum of first n odd numbers = n^2
    sum_odd = n * n
    
    # Sum of first n even numbers = n * (n + 1)
    sum_even = n * (n + 1)
    
    return math.gcd(sum_odd, sum_even)