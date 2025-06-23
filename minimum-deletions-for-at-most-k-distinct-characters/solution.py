from collections import Counter

def solve(s: str, k: int) -> int:
    """
    Calculate the minimum number of deletions required to ensure that
    the resulting string has at most k distinct characters.

    :param s: Input string consisting of lowercase English letters.
    :param k: Maximum number of distinct characters allowed in the resulting string.
    :return: Minimum number of deletions required.
    """
    if k >= len(set(s)):
        return 0

    freq = Counter(s)
    sorted_freq = sorted(freq.values(), reverse=True)

    deletions = 0
    for i in range(len(sorted_freq) - k):
        deletions += sorted_freq[i]

    return deletions