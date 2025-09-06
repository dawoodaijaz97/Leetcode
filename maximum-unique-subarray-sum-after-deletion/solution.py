def solve(nums: list[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    seen = set()

    for num in nums:
        if num not in seen:
            current_sum += num
            seen.add(num)
            max_sum = max(max_sum, current_sum)
        else:
            # If the number is already in the set, reset the current sum and seen set
            current_sum = 0
            seen.clear()

    return max_sum if max_sum != float('-inf') else 0