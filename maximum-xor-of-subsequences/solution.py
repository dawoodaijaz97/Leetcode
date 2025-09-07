def solve(nums: list[int]) -> int:
    max_xor = 0
    for num in nums:
        max_xor |= num
    return max_xor * 2

solve.__doc__ = """
Return the maximum possible value of X XOR Y where X and Y are bitwise XORs of two subsequences of nums.
"""