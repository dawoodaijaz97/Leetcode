def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    count = 0
    num_count = {}
    
    for num in nums:
        if num % 2 == 0:
            target = num // 2
            if target in num_count and num in num_count:
                count += num_count[target] * num_count[num]
                count %= MOD
        
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    return count