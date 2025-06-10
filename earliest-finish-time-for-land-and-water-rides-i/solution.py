def solve(landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
    min_finish_time = float('inf')
    
    for l_start, l_duration in zip(landStartTime, landDuration):
        l_end = l_start + l_duration
        for w_start, w_duration in zip(waterStartTime, waterDuration):
            if w_start >= l_end:
                finish_time = w_start + w_duration
            else:
                finish_time = max(l_end, w_start) + w_duration
            min_finish_time = min(min_finish_time, finish_time)
    
    for w_start, w_duration in zip(waterStartTime, waterDuration):
        w_end = w_start + w_duration
        for l_start, l_duration in zip(landStartTime, landDuration):
            if l_start >= w_end:
                finish_time = l_start + l_duration
            else:
                finish_time = max(w_end, l_start) + l_duration
            min_finish_time = min(min_finish_time, finish_time)
    
    return min_finish_time