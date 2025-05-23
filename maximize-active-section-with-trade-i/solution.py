def solve(s: str) -> int:
    # Augment the string with '1' at both ends
    t = '1' + s + '1'
    n = len(t)
    
    # Find all segments of '0's surrounded by '1's
    zero_segments = []
    start = -1
    for i in range(n):
        if t[i] == '0':
            if start == -1:
                start = i
        else:
            if start != -1:
                zero_segments.append((start, i))
                start = -1
    
    # If there are no valid segments to trade, return the number of '1's in the original string
    if not zero_segments:
        return s.count('1')
    
    # Calculate the maximum active sections after one optimal trade
    max_active_sections = 0
    for z_start, z_end in zero_segments:
        # Count '1's before and after the zero segment
        ones_before = t[:z_start].count('1')
        ones_after = t[z_end:].count('1')
        
        # Calculate the new number of active sections if we trade this segment
        new_active_sections = ones_before + ones_after + (z_end - z_start)
        
        # Update the maximum
        max_active_sections = max(max_active_sections, new_active_sections)
    
    return max_active_sections