from typing import List

def solve(digits: List[int]) -> int:
    count = 0
    digits_set = set(digits)
    
    for even in {0, 2, 4, 6, 8} & digits_set:
        if even == 0:
            # If the even digit is 0, we can't have leading zeros
            continue
        
        # Choose the first digit (non-zero and not equal to the even digit)
        for first in digits_set - {even, 0}:
            # Choose the second digit (can be any except the first and even digit)
            for second in digits_set - {first, even}:
                count += 1
    
    return count