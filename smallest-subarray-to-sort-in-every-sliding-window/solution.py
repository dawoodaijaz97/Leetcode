def solve(arr: list[int]) -> int:
    """
    Finds the smallest subarray that needs to be sorted in every sliding window of size 3.
    
    :param arr: List of integers
    :return: Length of the smallest subarray to sort
    """
    n = len(arr)
    if n < 3:
        return 0

    min_len = float('inf')

    for i in range(n - 2):
        window = arr[i:i+3]
        sorted_window = sorted(window)
        if window != sorted_window:
            # Find the smallest subarray that needs to be sorted
            left = next(j for j, x in enumerate(window) if x != sorted_window[j])
            right = next(j for j, x in enumerate(reversed(window)) if x != sorted_window[-j-1])
            min_len = min(min_len, right - left + 1)

    return min_len