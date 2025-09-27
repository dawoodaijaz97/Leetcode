def solve(nums: list[int], k: int) -> list[bool]:
    n = len(nums)
    dp = [False] * (k + 1)
    dp[0] = True

    for x in range(1, n + 1):
        new_dp = dp[:]
        cap_value = min(x, max(nums))
        for num in nums:
            if num <= cap_value:
                for j in range(k - num, -1, -1):
                    if dp[j]:
                        new_dp[j + num] = True
        dp = new_dp

    return [dp[k] for _ in range(n)]