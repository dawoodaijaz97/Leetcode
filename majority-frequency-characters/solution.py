from collections import Counter

def solve(s: str) -> str:
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Group characters by their frequency
    freq_groups = {}
    for char, count in freq.items():
        if count not in freq_groups:
            freq_groups[count] = set()
        freq_groups[count].add(char)
    
    # Find the majority frequency group
    max_group_size = 0
    majority_freq = 0
    for k, chars in freq_groups.items():
        if len(chars) > max_group_size or (len(chars) == max_group_size and k > majority_freq):
            max_group_size = len(chars)
            majority_freq = k
    
    # Return all characters in the majority frequency group
    return ''.join(freq_groups[majority_freq])