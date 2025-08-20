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

def solve(s: str) -> int:
    unique_primes = set()
    
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            num_str = s[start:end].lstrip('0')
            if num_str and is_prime(int(num_str)):
                unique_primes.add(int(num_str))
    
    sorted_primes = sorted(unique_primes, reverse=True)
    return sum(sorted_primes[:3])