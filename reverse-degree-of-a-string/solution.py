def solve(s: str) -> int:
    """
    Calculate the reverse degree of a given string.

    :param s: Input string consisting of lowercase English letters.
    :return: The reverse degree of the string.
    """
    reversed_degree = 0
    for index, char in enumerate(s, start=1):
        reversed_alphabet_index = 27 - (ord(char) - ord('a'))
        reversed_degree += reversed_alphabet_index * index
    return reversed_degree