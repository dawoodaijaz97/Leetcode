def solve(s: str, queries: list[list[int]]) -> list[int]:
    n = len(s)
    
    # Calculate prefix sums to quickly count '1's in any substring
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + (s[i] == '1')
    
    def count_ones_in_range(l: int, r: int) -> int:
        return prefix_sum[r + 1] - prefix_sum[l]
    
    # Find all blocks of '1's surrounded by '0's
    blocks = []
    i = 0
    while i < n:
        if s[i] == '0':
            start = i
            while i < n and s[i] == '0':
                i += 1
            end = i - 1
            if start > 0 and end < n - 1 and s[start - 1] == '1' and s[end + 1] == '1':
                blocks.append((start, end))
        else:
            i += 1
    
    # For each query, determine the maximum possible number of active sections
    result = []
    for l, r in queries:
        augmented_s = '1' + s[l:r+1] + '1'
        max_active_sections = count_ones_in_range(0, len(augmented_s) - 1)
        
        # Try to perform a trade on each valid block
        for start, end in blocks:
            if l <= start and end <= r:
                # Calculate the new number of active sections after the trade
                new_active_sections = (
                    count_ones_in_range(0, start) +
                    (end - start + 1) +  # All '1's in the block become '0's
                    count_ones_in_range(end + 1, len(augmented_s) - 1)
                )
                max_active_sections = max(max_active_sections, new_active_sections)
        
        result.append(max_active_sections)
    
    return result