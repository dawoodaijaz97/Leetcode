def solve(cost: list[int]) -> list[int]:
    n = len(cost)
    answer = [float('inf')] * n
    answer[0] = cost[0]
    
    for i in range(1, n):
        answer[i] = min(answer[i], answer[i - 1] + cost[i])
        if i > 1:
            answer[i] = min(answer[i], answer[i - 2] + cost[i])
    
    return answer