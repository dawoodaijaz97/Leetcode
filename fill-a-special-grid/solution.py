def solve(n: int) -> list[list[int]]:
    def fill_grid(size: int, offset: int) -> list[list[int]]:
        if size == 1:
            return [[offset]]
        
        half_size = size // 2
        top_left = fill_grid(half_size, offset + (3 * half_size * half_size))
        top_right = fill_grid(half_size, offset + (2 * half_size * half_size))
        bottom_left = fill_grid(half_size, offset + (half_size * half_size))
        bottom_right = fill_grid(half_size, offset)
        
        grid = [[0] * size for _ in range(size)]
        for i in range(half_size):
            for j in range(half_size):
                grid[i][j] = top_left[i][j]
                grid[i][j + half_size] = top_right[i][j]
                grid[i + half_size][j] = bottom_left[i][j]
                grid[i + half_size][j + half_size] = bottom_right[i][j]
        
        return grid
    
    return fill_grid(2 ** n, 0)