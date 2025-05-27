def solve(nums: list[int]) -> int:
    """
    Maximize the score after pair deletions.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The maximum score.
    """
    from collections import Counter

    # Count the frequency of each number
    freq = Counter(nums)
    
    max_score = 0
    
    for num, count in freq.items():
        # Calculate the contribution of this number to the score
        pairs = count // 2
        max_score += pairs * (num ** 2)
    
    return max_score