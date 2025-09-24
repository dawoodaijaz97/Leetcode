def solve(nums: list[int]) -> int:
    average = sum(nums) / len(nums)
    positive_integers = {num for num in nums if num > 0}
    
    i = 1
    while True:
        if i not in positive_integers and i > average:
            return i
        i += 1