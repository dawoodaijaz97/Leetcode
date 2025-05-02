def solve(strings: list[str]) -> str:
    """
    Finds the shortest superstring that contains each string in the input list as a substring.
    
    :param strings: List of strings to be combined into a superstring.
    :return: The shortest superstring containing all input strings.
    """
    from itertools import permutations

    def merge(a: str, b: str) -> str:
        """Merge two strings by finding the longest common suffix/prefix overlap."""
        max_overlap = 0
        for i in range(1, min(len(a), len(b)) + 1):
            if a[-i:] == b[:i]:
                max_overlap = i
        return a + b[max_overlap:]

    # Generate all permutations of the input strings
    perms = permutations(strings)
    
    # Initialize the shortest superstring with a large value
    shortest_superstring = ''.join(strings) * len(strings)
    
    # Check each permutation to find the shortest superstring
    for perm in perms:
        current_superstring = perm[0]
        for i in range(1, len(perm)):
            current_superstring = merge(current_superstring, perm[i])
        
        if len(current_superstring) < len(shortest_superstring):
            shortest_superstring = current_superstring
    
    return shortest_superstring