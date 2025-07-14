from typing import List

def solve(poly1: List[int], poly2: List[int]) -> List[int]:
    """
    Multiplies two polynomials represented by lists of coefficients.
    
    Args:
        poly1 (List[int]): Coefficients of the first polynomial.
        poly2 (List[int]): Coefficients of the second polynomial.
        
    Returns:
        List[int]: Coefficients of the resulting polynomial.
    """
    result_length = len(poly1) + len(poly2) - 1
    result = [0] * result_length
    
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    
    return result