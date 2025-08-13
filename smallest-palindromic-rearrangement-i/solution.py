def solve(s: str) -> str:
    from collections import Counter
    
    # Count frequency of each character
    char_count = Counter(s)
    
    # Create half of the palindrome by sorting characters lexicographically
    half_palindrome = ''.join(sorted(char // 2 for char in char_count.values()))
    
    # If the length of s is odd, find the middle character
    middle_char = ''
    if len(s) % 2 == 1:
        for char, count in char_count.items():
            if count % 2 == 1:
                middle_char = char
                break
    
    # Construct the full palindrome
    return half_palindrome + middle_char + half_palindrome[::-1]