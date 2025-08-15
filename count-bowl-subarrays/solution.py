def solve(nums: list[int]) -> int:
    n = len(nums)
    bowl_count = 0

    for i in range(n):
        min_val = nums[i]
        max_val = float('-inf')
        valid = False

        for j in range(i + 1, n):
            if nums[j] < min_val and nums[j] > max_val:
                valid = True
            elif nums[j] >= min_val:
                break
            else:
                max_val = max(max_val, nums[j])

            if valid and j - i + 1 >= 3:
                bowl_count += 1

    return bowl_count