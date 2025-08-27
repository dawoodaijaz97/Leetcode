def solve(days_late: int, daily_fee: float) -> float:
    """
    Calculate the total late fee for books returned late to the library.

    :param days_late: Number of days the book is overdue.
    :param daily_fee: Fee per day the book is overdue.
    :return: Total late fee.
    """
    return max(0, days_late * daily_fee)