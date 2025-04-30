def solve(s: str) -> int:
    vowels = set('aeiou')
    vowel_count = 0
    consonant_count = 0
    
    max_vowel_freq = 0
    max_consonant_freq = 0
    
    for char in s:
        if char in vowels:
            vowel_count += 1
            if vowel_count > max_vowel_freq:
                max_vowel_freq = vowel_count
        else:
            consonant_count += 1
            if consonant_count > max_consonant_freq:
                max_consonant_freq = consonant_count
    
    return max_vowel_freq + max_consonant_freq