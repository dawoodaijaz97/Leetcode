def solve(nums: list[int]) -> int:
    max_product = 0
    n = len(nums)
    
    # Sort numbers in descending order
    nums.sort(reverse=True)
    
    # Precompute the bitwise AND of all pairs to check for common bits
    and_results = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            and_results[i][j] = nums[i] & nums[j]
    
    # Iterate over all pairs to find the maximum product with no common bits
    for i in range(n):
        for j in range(i + 1, n):
            if and_results[i][j] == 0:
                max_product = max(max_product, nums[i] * nums[j])
    
    return max_product