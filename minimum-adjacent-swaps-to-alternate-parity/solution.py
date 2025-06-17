def solve(nums: list[int]) -> int:
    def count_swaps(start_with_even: bool) -> int:
        swaps = 0
        even_index, odd_index = 0, 0
        n = len(nums)
        
        for i in range(n):
            if (i % 2 == start_with_even and nums[i] % 2 != 0) or \
               (i % 2 != start_with_even and nums[i] % 2 == 0):
                while (even_index < n and nums[even_index] % 2 == start_with_even) or \
                      (odd_index < n and nums[odd_index] % 2 != start_with_even):
                    if even_index < n and nums[even_index] % 2 == start_with_even:
                        even_index += 1
                    if odd_index < n and nums[odd_index] % 2 != start_with_even:
                        odd_index += 1
                
                if i % 2 == start_with_even:
                    swaps += n - even_index
                    nums[i], nums[even_index] = nums[even_index], nums[i]
                    even_index += 1
                else:
                    swaps += n - odd_index
                    nums[i], nums[odd_index] = nums[odd_index], nums[i]
                    odd_index += 1
        
        return swaps

    even_count = sum(1 for x in nums if x % 2 == 0)
    odd_count = len(nums) - even_count
    
    if abs(even_count - odd_count) > 1:
        return -1
    
    if even_count >= odd_count:
        return count_swaps(True)
    else:
        return count_swaps(False)