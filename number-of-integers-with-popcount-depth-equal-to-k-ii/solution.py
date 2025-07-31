def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    def popcount_depth(x: int) -> int:
        depth = 0
        while x != 1:
            x = bin(x).count('1')
            depth += 1
        return depth

    n = len(nums)
    depths = [popcount_depth(num) for num in nums]
    
    def count_in_range(l: int, r: int, k: int) -> int:
        return sum(1 for i in range(l, r + 1) if depths[i] == k)

    answers = []
    for query in queries:
        if query[0] == 1:
            l, r, k = query[1], query[2], query[3]
            answers.append(count_in_range(l, r, k))
        elif query[0] == 2:
            idx, val = query[1], query[2]
            depths[idx] = popcount_depth(val)

    return answers