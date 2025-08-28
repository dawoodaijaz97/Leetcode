from collections import Counter
from typing import List

def solve(words: List[str], k: int) -> List[int]:
    def longest_common_prefix(strs: List[str]) -> int:
        if not strs:
            return 0
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return 0
        return len(prefix)
    
    word_count = Counter(words)
    unique_words = list(word_count.keys())
    answer = []
    
    for i, word in enumerate(words):
        if word_count[word] == 1:
            remaining_words = [w for w in words if w != word]
        else:
            remaining_words = words[:]
            remaining_words.remove(word)
        
        if len(remaining_words) < k:
            answer.append(0)
        else:
            top_k_words = []
            for _ in range(k):
                max_count = max(word_count.values())
                most_common_word = next(w for w, count in word_count.items() if count == max_count)
                top_k_words.append(most_common_word)
                word_count[most_common_word] -= 1
            
            answer.append(longest_common_prefix(top_k_words))
    
    return answer