def solve(nums: list[int]) -> int:
    """
    Calculate the minimum number of operations required to convert all elements in the array to zero.
    
    :param nums: List of non-negative integers.
    :return: Minimum number of operations.
    """
    unique_values = set(nums)
    return len(unique_values) - (0 in unique_values)