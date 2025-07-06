def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(n))

def solve(nums: list[int]) -> int:
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort(key=lambda x: (digit_sum(x[0]), x[0]))
    
    visited = [False] * len(nums)
    swaps = 0
    
    for i in range(len(nums)):
        if visited[i] or indexed_nums[i][1] == i:
            continue
        
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = indexed_nums[j][1]
            cycle_size += 1
        
        if cycle_size > 1:
            swaps += (cycle_size - 1)
    
    return swaps