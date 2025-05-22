def solve(arr: list[int]) -> list[int]:
    """
    Convert all negative numbers in the input array to positive.

    :param arr: List of integers.
    :return: A new list with all negative numbers converted to positive.
    """
    return [abs(x) for x in arr]