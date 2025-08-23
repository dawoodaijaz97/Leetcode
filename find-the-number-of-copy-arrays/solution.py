def solve(original: list[int], bounds: list[list[int]]) -> int:
    MOD = 1_000_000_007
    n = len(original)
    
    # Calculate the required difference between consecutive elements
    diff = original[1] - original[0]
    
    # Initialize the number of valid arrays
    count = 1
    
    for i in range(1, n):
        # Calculate the new bounds based on the required difference
        lower_bound = max(bounds[i][0], original[i] - diff)
        upper_bound = min(bounds[i][1], original[i] - diff)
        
        # If the new bounds are valid, count the number of possible values
        if lower_bound <= upper_bound:
            count = (count * (upper_bound - lower_bound + 1)) % MOD
        else:
            # If no valid value is found, return 0
            return 0
    
    return count