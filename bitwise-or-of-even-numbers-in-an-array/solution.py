def solve(nums: list[int]) -> int:
    """
    Return the bitwise OR of all even numbers in the array.
    If there are no even numbers, return 0.

    :param nums: List of integers
    :return: Bitwise OR of even numbers
    """
    result = 0
    for num in nums:
        if num % 2 == 0:
            result |= num
    return result