def solve(s: str) -> int:
    """
    Calculate the minimum number of operations required to transform
    the string `s` into a string consisting only of 'a' characters.
    
    :param s: Input string consisting of lowercase English letters.
    :return: Minimum number of operations.
    """
    return sum(min(ord(c) - ord('a'), ord('z') - ord(c) + 1) for c in s)