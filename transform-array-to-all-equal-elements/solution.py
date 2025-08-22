def solve(nums: list[int], k: int) -> bool:
    """
    Determine if it's possible to make all elements of the array equal
    by performing at most k operations, where each operation allows
    multiplying both nums[i] and nums[i + 1] by -1.

    :param nums: List of integers containing only 1 and -1.
    :param k: Maximum number of operations allowed.
    :return: True if all elements can be made equal, False otherwise.
    """
    # Count the number of adjacent pairs that are different
    flips_needed = sum(nums[i] != nums[i + 1] for i in range(len(nums) - 1))
    
    # We need at least half of these flips to make all elements equal
    return flips_needed // 2 <= k