from collections import Counter

def solve(n: int) -> int:
    """
    Find the least frequent digit in the decimal representation of an integer n.
    If multiple digits have the same frequency, return the smallest digit.
    
    :param n: Integer to analyze
    :return: The least frequent digit as an integer
    """
    # Convert the number to a string and count the frequency of each digit
    digit_counts = Counter(str(n))
    
    # Find the minimum frequency
    min_frequency = min(digit_counts.values())
    
    # Find the smallest digit with the minimum frequency
    least_frequent_digit = min(int(digit) for digit, count in digit_counts.items() if count == min_frequency)
    
    return least_frequent_digit