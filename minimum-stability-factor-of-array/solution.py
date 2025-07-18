from typing import List

def solve(nums: List[int], maxC: int) -> int:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    n = len(nums)
    if maxC >= n - 1:
        return 1

    # Find the minimum possible stability factor
    min_stability_factor = 0
    for i in range(n):
        current_hcf = nums[i]
        for j in range(i + 1, n):
            current_hcf = gcd(current_hcf, nums[j])
            if current_hcf < 2:
                break
            min_stability_factor = max(min_stability_factor, j - i + 1)

    # If no stable subarray is found, return 0
    if min_stability_factor == 0:
        return 0

    # Binary search to find the minimum possible stability factor after at most maxC modifications
    left, right = 2, n
    while left < right:
        mid = (left + right) // 2
        possible = False
        for i in range(n):
            count_modifications = 0
            current_hcf = nums[i]
            for j in range(i, min(i + mid, n)):
                current_hcf = gcd(current_hcf, nums[j])
                if current_hcf < 2:
                    count_modifications += 1
                    if count_modifications > maxC:
                        break
            if count_modifications <= maxC and current_hcf >= 2:
                possible = True
                break
        if possible:
            right = mid
        else:
            left = mid + 1

    return left