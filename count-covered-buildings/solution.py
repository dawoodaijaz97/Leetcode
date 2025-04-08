def solve(n: int, buildings: list[list[int]]) -> int:
    # Create sets for each row and column to track building presence
    rows = [set() for _ in range(n + 1)]
    cols = [set() for _ in range(n + 1)]
    
    # Populate the sets with building coordinates
    for x, y in buildings:
        rows[x].add(y)
        cols[y].add(x)
    
    covered_count = 0
    
    # Check each building to see if it is covered
    for x, y in buildings:
        # A building is covered if there are buildings in all four directions
        if (len(rows[x]) > 1 and len(cols[y]) > 1):
            above = any(y2 < y for y2 in rows[x])
            below = any(y2 > y for y2 in rows[x])
            left = any(x2 < x for x2 in cols[y])
            right = any(x2 > x for x2 in cols[y])
            
            if above and below and left and right:
                covered_count += 1
    
    return covered_count