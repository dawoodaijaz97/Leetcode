def solve(words: list[str]) -> int:
    """
    Finds the maximum distance between two unequal words in the given list.
    
    :param words: List of words (strings).
    :return: Maximum distance between two unequal words.
    """
    max_distance = 0
    word_set = set(words)
    
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words[i+1:], start=i+1):
            if word1 != word2:
                max_distance = max(max_distance, j - i)
    
    return max_distance