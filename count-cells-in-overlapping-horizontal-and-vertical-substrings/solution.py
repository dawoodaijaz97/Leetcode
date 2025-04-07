def solve(grid: list[list[str]], pattern: str) -> int:
    m, n = len(grid), len(grid[0])
    pattern_length = len(pattern)
    
    def matches_horizontal(x: int, y: int) -> bool:
        for i in range(pattern_length):
            if grid[(x + i) % m][y] != pattern[i]:
                return False
        return True
    
    def matches_vertical(x: int, y: int) -> bool:
        for i in range(pattern_length):
            if grid[x][(y + i) % n] != pattern[i]:
                return False
        return True
    
    count = 0
    for x in range(m):
        for y in range(n):
            if matches_horizontal(x, y) and matches_vertical(x, y):
                count += 1
    
    return count