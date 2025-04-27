from typing import List

def solve(coords: List[List[int]]) -> int:
    max_area = 0
    x_coords = {}
    y_coords = {}

    for x, y in coords:
        if x not in x_coords:
            x_coords[x] = []
        x_coords[x].append(y)
        
        if y not in y_coords:
            y_coords[y] = []
        y_coords[y].append(x)

    for x in x_coords:
        x_coords[x].sort()

    for y in y_coords:
        y_coords[y].sort()

    for i in range(len(coords)):
        x1, y1 = coords[i]
        
        if len(x_coords[x1]) > 1:
            max_height = 0
            for j in range(1, len(x_coords[x1])):
                max_height = max(max_height, abs(x_coords[x1][j] - x_coords[x1][j-1]))
            
            if max_height > 0:
                base = max(y_coords[y1][0], y_coords[y1][-1]) - min(y_coords[y1][0], y_coords[y1][-1])
                max_area = max(max_area, max_height * base)

        if len(y_coords[y1]) > 1:
            max_width = 0
            for j in range(1, len(y_coords[y1])):
                max_width = max(max_width, abs(y_coords[y1][j] - y_coords[y1][j-1]))
            
            if max_width > 0:
                base = max(x_coords[x1][0], x_coords[x1][-1]) - min(x_coords[x1][0], x_coords[x1][-1])
                max_area = max(max_area, max_width * base)

    return 2 * max_area if max_area > 0 else -1