def solve(nums: list[int], k: int) -> list[int]:
    """
    Solve the problem of maximizing the sum of at most k distinct elements from nums.
    
    :param nums: List of positive integers.
    :param k: Maximum number of distinct elements to choose.
    :return: List of chosen numbers in strictly descending order.
    """
    # Use a set to get unique elements and sort them in descending order
    unique_nums = sorted(set(nums), reverse=True)
    
    # Return the first k elements from the sorted unique list
    return unique_nums[:k]