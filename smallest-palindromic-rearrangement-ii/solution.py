from collections import Counter
import math

def solve(s: str, k: int) -> str:
    # Count frequency of each character
    freq = Counter(s)
    
    # Calculate the number of distinct palindromic permutations
    def count_permutations(freq):
        total = math.factorial(len(s) // 2)
        for v in freq.values():
            if v % 2 == 0:
                total //= math.factorial(v // 2)
            else:
                total //= math.factorial((v - 1) // 2)
        return total
    
    # If there are fewer than k distinct palindromic permutations, return an empty string
    if count_permutations(freq) < k:
        return ""
    
    # Find the k-th lexicographically smallest palindromic permutation
    def find_kth_palindrome(freq, k):
        half = []
        for char in sorted(freq.keys()):
            if freq[char] % 2 == 1:
                middle = char
                freq[char] -= 1
            else:
                half.extend([char] * (freq[char] // 2))
        
        def next_permutation(arr):
            n = len(arr)
            i = n - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return False
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True
        
        # Generate the k-th permutation of half
        for _ in range(k - 1):
            if not next_permutation(half):
                return ""
        
        # Construct the full palindrome
        first_half = ''.join(half)
        second_half = first_half[::-1]
        if 'middle' in locals():
            return first_half + middle + second_half
        else:
            return first_half + second_half
    
    return find_kth_palindrome(freq, k)