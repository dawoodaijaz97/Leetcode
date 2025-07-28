from typing import List

def solve(robots: List[int], distance: List[int], walls: List[int]) -> int:
    """
    Calculate the maximum number of unique walls that can be destroyed by robots.

    :param robots: List of robot positions.
    :param distance: List of maximum distances each robot's bullet can travel.
    :param walls: List of wall positions.
    :return: Maximum number of unique walls that can be destroyed.
    """
    # Sort walls for efficient range checking
    walls.sort()
    
    # Use a set to track unique walls destroyed
    destroyed_walls = set()
    
    for i, robot in enumerate(robots):
        max_range = distance[i]
        
        # Calculate the left and right bounds of the bullet's range
        left_bound = robot - max_range
        right_bound = robot + max_range
        
        # Find the first wall within the range using binary search
        left_index = bisect_left(walls, left_bound)
        right_index = bisect_right(walls, right_bound)
        
        # Add all walls within the range to the set of destroyed walls
        for j in range(left_index, right_index):
            if walls[j] >= robot:
                break  # Stop at the first wall that is on or after the robot
            destroyed_walls.add(walls[j])
    
    return len(destroyed_walls)

from bisect import bisect_left, bisect_right