from typing import List

def solve(n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
    def dfs(state: int, stage: int) -> float:
        if state == (1 << n) - 1:
            return 0.0
        
        min_time = float('inf')
        for group in range(1, 1 << n):
            if bin(group).count('1') > k:
                continue
            if state & group != group:
                continue
            
            max_time = max(time[i] for i in range(n) if (group >> i) & 1)
            crossing_time = max_time * mul[stage]
            next_stage = (stage + int(crossing_time)) % m
            remaining_state = state ^ group
            
            return_time = min(time[i] * mul[next_stage] for i in range(n) if (remaining_state >> i) & 1)
            total_time = crossing_time + return_time + dfs(remaining_state, next_stage)
            
            min_time = min(min_time, total_time)
        
        return min_time
    
    result = dfs(0, 0)
    return round(result, 5) if result != float('inf') else -1.0