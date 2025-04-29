def solve(n: int, m: int, k: int) -> int:
    def min_cost(log_length: int, truck_capacity: int) -> int:
        if log_length <= truck_capacity:
            return 0
        cost = float('inf')
        for i in range(1, log_length):
            cost = min(cost, i * (log_length - i) + min_cost(i, truck_capacity) + min_cost(log_length - i, truck_capacity))
        return cost

    return min_cost(n, k) + min_cost(m, k)