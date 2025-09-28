from collections import Counter
from typing import List

def solve(arr: List[int], weights: List[int]) -> int:
    """
    Calculate the sum of weighted modes in all subarrays.

    :param arr: List of integers representing the array.
    :param weights: List of integers representing the weights for each element in the array.
    :return: Sum of weighted modes in all subarrays.
    """
    n = len(arr)
    total_sum = 0

    for start in range(n):
        frequency = Counter()
        max_weight = 0
        mode_count = 0

        for end in range(start, n):
            frequency[arr[end]] += weights[end]
            
            if frequency[arr[end]] > max_weight:
                max_weight = frequency[arr[end]]
                mode_count = 1
            elif frequency[arr[end]] == max_weight:
                mode_count += 1

            total_sum += mode_count * max_weight

    return total_sum