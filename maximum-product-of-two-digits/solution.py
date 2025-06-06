def solve(n: int) -> int:
    # Convert the number to a string to iterate over each digit
    digits = str(n)
    
    # Initialize the maximum product to 0
    max_product = 0
    
    # Iterate over each pair of digits
    for i in range(len(digits)):
        for j in range(i, len(digits)):
            # Convert the characters back to integers and calculate the product
            product = int(digits[i]) * int(digits[j])
            
            # Update the maximum product if the current one is greater
            if product > max_product:
                max_product = product
    
    return max_product