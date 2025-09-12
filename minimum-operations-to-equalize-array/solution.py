def solve(nums: list[int]) -> int:
    """
    Calculate the minimum number of operations required to make all elements of nums equal.
    
    :param nums: List of integers representing the array.
    :return: Minimum number of operations.
    """
    if not nums:
        return 0
    
    # The bitwise AND of all numbers will be the target value for all elements
    target = nums[0]
    for num in nums:
        target &= num
    
    # If all numbers are already equal, no operations are needed
    if all(num == target for num in nums):
        return 0
    
    # Otherwise, we need at least one operation to make all elements equal to the target
    return 1