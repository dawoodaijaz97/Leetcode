def solve(s: str, k: int) -> int:
    """
    Calculate the minimum number of operations required to make all characters in the binary string equal to '1'.
    
    :param s: Binary string consisting of '0's and '1's.
    :param k: Number of indices to flip in each operation.
    :return: Minimum number of operations if possible, otherwise -1.
    """
    n = len(s)
    zero_count = s.count('0')
    
    # If the number of zeros is not divisible by k, it's impossible to make all '1's
    if zero_count % k != 0:
        return -1
    
    # Calculate the minimum number of operations
    operations = zero_count // k
    return operations