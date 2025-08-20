from collections import Counter

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    def query(l: int, r: int, threshold: int) -> int:
        subarray = nums[l:r+1]
        frequency = Counter(subarray)
        max_freq = 0
        result = -1
        
        for num, freq in frequency.items():
            if freq >= threshold:
                if freq > max_freq or (freq == max_freq and num < result):
                    max_freq = freq
                    result = num
        
        return result
    
    return [query(l, r, threshold) for l, r, threshold in queries]