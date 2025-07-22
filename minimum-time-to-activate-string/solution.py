def solve(s: str, order: list[int], k: int) -> int:
    n = len(s)
    active_count = 0
    star_positions = set()
    
    def count_valid_substrings():
        nonlocal active_count
        active_count = 0
        for i in range(n):
            if s[i] == '*':
                continue
            for j in range(i, n):
                if '*' in s[i:j+1]:
                    active_count += 1
    
    for t in range(n):
        index = order[t]
        s = s[:index] + '*' + s[index+1:]
        star_positions.add(index)
        count_valid_substrings()
        if active_count >= k:
            return t
    
    return -1