from collections import Counter
from typing import List, Tuple

def solve(s: str, k: int) -> str:
    """
    Filter characters from string s that appear at least k times.
    
    Args:
        s: Input string
        k: Minimum frequency threshold
        
    Returns:
        String with characters appearing at least k times
    """
    char_count = Counter(s)
    return ''.join(char for char, count in char_count.items() if count >= k)