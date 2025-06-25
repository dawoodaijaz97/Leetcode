def solve(weight: list[int]) -> int:
    n = len(weight)
    max_weight = [0] * n
    current_max = 0
    
    for i in range(n):
        current_max = max(current_max, weight[i])
        max_weight[i] = current_max
    
    count = 0
    last_shipment_end = -1
    
    for i in range(n - 1, last_shipment_end, -1):
        if weight[i] < max_weight[i]:
            count += 1
            last_shipment_end = i - 1
    
    return count