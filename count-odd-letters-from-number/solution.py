def solve(number: int) -> int:
    """
    Count the number of odd digits in the given integer.

    :param number: The integer to analyze.
    :return: The count of odd digits in the integer.
    """
    return sum(1 for digit in str(abs(number)) if int(digit) % 2 != 0)