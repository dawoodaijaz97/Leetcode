def solve(x: int, y: int, z: int) -> int:
    distance_x = abs(z - x)
    distance_y = abs(z - y)
    
    if distance_x < distance_y:
        return 1
    elif distance_y < distance_x:
        return 2
    else:
        return 0