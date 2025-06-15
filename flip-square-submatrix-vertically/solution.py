def solve(grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
    """
    Flips a square submatrix of size k x k in the grid starting from (x, y) vertically.

    :param grid: List of lists representing the matrix.
    :param x: Row index of the top-left corner of the submatrix.
    :param y: Column index of the top-left corner of the submatrix.
    :param k: Size of the square submatrix to flip.
    :return: The updated grid with the specified submatrix flipped vertically.
    """
    # Flip the rows in the specified submatrix
    for i in range(k // 2):
        for j in range(k):
            top = grid[x + i][y + j]
            bottom = grid[x + k - 1 - i][y + j]
            grid[x + i][y + j] = bottom
            grid[x + k - 1 - i][y + j] = top

    return grid