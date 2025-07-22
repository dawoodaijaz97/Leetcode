def solve(nums: list[int]) -> int:
    unique_xor_values = set()
    
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                xor_value = nums[i] ^ nums[j] ^ nums[k]
                unique_xor_values.add(xor_value)
    
    return len(unique_xor_values)