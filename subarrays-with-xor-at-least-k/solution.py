from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Counts the number of subarrays in `nums` such that the XOR of the subarray is at least `k`.

    :param nums: List of integers.
    :param k: Integer representing the minimum XOR value for a subarray.
    :return: Number of subarrays with XOR at least `k`.
    """
    count = 0
    prefix_xor = 0
    xor_count = {0: 1}

    for num in nums:
        prefix_xor ^= num
        target = prefix_xor ^ k
        if target in xor_count:
            count += xor_count[target]
        if prefix_xor in xor_count:
            xor_count[prefix_xor] += 1
        else:
            xor_count[prefix_xor] = 1

    return count