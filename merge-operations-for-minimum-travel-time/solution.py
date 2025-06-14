from typing import List

def solve(l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
    # Calculate initial travel times for each segment
    travel_times = [time[i] * (position[i + 1] - position[i]) for i in range(n - 1)]
    
    # Perform k merge operations to minimize total travel time
    for _ in range(k):
        min_index = 0
        min_time_increase = float('inf')
        
        # Find the merge that results in the smallest increase in travel time
        for i in range(1, n - 2):
            new_time = (position[i + 2] - position[i]) * (time[i] + time[i + 1])
            current_time = travel_times[i] + travel_times[i + 1]
            if new_time < current_time:
                time_increase = new_time - current_time
                if time_increase < min_time_increase:
                    min_time_increase = time_increase
                    min_index = i
        
        # Perform the merge operation
        if min_time_increase != float('inf'):
            travel_times[min_index] = (position[min_index + 2] - position[min_index]) * (time[min_index] + time[min_index + 1])
            del travel_times[min_index + 1]
            del time[min_index + 1]
    
    # Calculate the final total travel time
    return sum(travel_times)