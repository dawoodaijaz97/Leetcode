def solve(order: list[int], friends: list[int]) -> list[int]:
    """
    Returns the finishing order of friends based on the given race order.

    :param order: List of integers representing the finishing order of participants.
    :param friends: List of integers representing the IDs of friends in strictly increasing order.
    :return: List of integers representing the finishing order of friends.
    """
    friend_set = set(friends)
    return [participant for participant in order if participant in friend_set]