def solve(n: int, m: int, k: int) -> int:
    """
    Calculate the minimum number of sensors required to cover an n x m grid,
    where each sensor covers cells within Chebyshev distance k.
    
    :param n: Number of rows in the grid
    :param m: Number of columns in the grid
    :param k: Maximum Chebyshev distance a sensor can cover
    :return: Minimum number of sensors needed to cover the entire grid
    """
    if k == 0:
        return n * m
    
    # Calculate the effective coverage area of one sensor
    effective_coverage = (2 * k + 1) ** 2
    
    # Calculate the minimum number of sensors needed
    min_sensors = (n * m + effective_coverage - 1) // effective_coverage
    
    return min_sensors