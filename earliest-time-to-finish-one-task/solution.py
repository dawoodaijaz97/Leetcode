def solve(tasks: list[list[int]]) -> int:
    """
    Finds the earliest time at which at least one task is finished.

    :param tasks: A 2D list where each element is [start_time, duration].
    :return: The earliest finish time of any task.
    """
    return max(start + duration for start, duration in tasks)