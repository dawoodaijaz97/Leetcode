def solve(n: int, w: int, maxWeight: int) -> int:
    """
    Calculate the maximum number of containers that can be loaded onto a ship.

    :param n: Size of the cargo deck (n x n)
    :param w: Weight of each container
    :param maxWeight: Maximum weight capacity of the ship
    :return: Maximum number of containers that can be loaded
    """
    total_cells = n * n
    max_containers = min(total_cells, maxWeight // w)
    return max_containers