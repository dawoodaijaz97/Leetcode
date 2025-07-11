def solve(sx: int, sy: int, tx: int, ty: int) -> int:
    """
    Calculate the minimum number of moves required to reach (tx, ty) from (sx, sy)
    on an infinitely large 2D grid using the allowed moves.
    
    :param sx: Starting x-coordinate
    :param sy: Starting y-coordinate
    :param tx: Target x-coordinate
    :param ty: Target y-coordinate
    :return: Minimum number of moves or -1 if it's impossible to reach the target
    """
    while tx >= sx and ty >= sy:
        if tx == sx:
            return (ty - sy) // max(sx, sy)
        if ty == sy:
            return (tx - sx) // max(sx, sy)
        
        if tx > ty:
            tx %= ty
        else:
            ty %= tx
    
    return -1