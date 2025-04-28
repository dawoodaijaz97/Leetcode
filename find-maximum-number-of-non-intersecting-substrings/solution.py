def solve(word: str) -> int:
    """
    Finds the maximum number of non-intersecting substrings in the given word
    that are at least four characters long and start and end with the same letter.
    
    :param word: The input string to analyze.
    :return: The maximum number of non-intersecting substrings meeting the criteria.
    """
    from collections import defaultdict

    # Dictionary to store the first and last occurrence of each character
    char_indices = defaultdict(lambda: [float('inf'), float('-inf')])
    
    for i, char in enumerate(word):
        if char_indices[char][0] == float('inf'):
            char_indices[char][0] = i
        char_indices[char][1] = i

    # List to store valid substrings as tuples (start_index, end_index)
    valid_substrings = []

    for start, end in char_indices.values():
        if end - start >= 3:
            valid_substrings.append((start, end))

    # Sort substrings by their end index
    valid_substrings.sort(key=lambda x: x[1])

    # Use a greedy algorithm to find non-intersecting substrings
    count = 0
    last_end = float('-inf')

    for start, end in valid_substrings:
        if start > last_end:
            count += 1
            last_end = end

    return count