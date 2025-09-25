def solve(arr: list) -> list:
    """
    Sorts an array by the absolute value of its elements.

    :param arr: List of integers to sort.
    :return: A new list sorted by the absolute values of the elements.
    """
    return sorted(arr, key=abs)