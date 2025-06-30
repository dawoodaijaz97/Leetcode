def solve(nums: list[int], k: int) -> int:
    total_sum = sum(nums)
    remainder = total_sum % k
    if remainder == 0:
        return 0
    
    min_operations = float('inf')
    for num in nums:
        # Calculate the number of operations needed to reduce this number
        # such that its contribution to the total remainder is minimized.
        operations = (num - remainder) % k
        min_operations = min(min_operations, operations)
    
    return min_operations