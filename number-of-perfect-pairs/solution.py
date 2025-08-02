def solve(nums: list[int]) -> int:
    def is_perfect_pair(a: int, b: int) -> bool:
        min_val = min(abs(a - b), abs(a + b))
        max_val = max(abs(a - b), abs(a + b))
        return min(min_val, abs(a), abs(b)) == min_val and max(max_val, abs(a), abs(b)) == max_val

    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if is_perfect_pair(nums[i], nums[j]):
                count += 1
    return count