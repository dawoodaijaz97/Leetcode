def solve(n: int, k: int) -> int:
    def popcount(x: int) -> int:
        return bin(x).count('1')
    
    def popcount_depth(x: int) -> int:
        depth = 0
        while x != 1:
            x = popcount(x)
            depth += 1
        return depth
    
    count = 0
    for i in range(1, n + 1):
        if popcount_depth(i) == k:
            count += 1
    return count