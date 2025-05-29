from typing import List
import math

def solve(nums: List[int], k: int) -> int:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    n = len(nums)
    max_score = 0

    # Precompute the GCDs for all subarrays
    gcd_cache = [[0] * n for _ in range(n)]
    for i in range(n):
        gcd_cache[i][i] = nums[i]
        for j in range(i + 1, n):
            gcd_cache[i][j] = gcd(gcd_cache[i][j - 1], nums[j])

    # Try to maximize the score by considering each subarray
    for i in range(n):
        for j in range(i, n):
            current_gcd = gcd_cache[i][j]
            # Calculate the maximum possible GCD after at most k doublings
            max_possible_gcd = current_gcd * (2 ** min(k, j - i + 1))
            score = (j - i + 1) * max_possible_gcd
            max_score = max(max_score, score)

    return max_score