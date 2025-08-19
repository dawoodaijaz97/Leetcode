def solve(s: str, k: int) -> int:
    from collections import defaultdict

    # Calculate prefix sums for U, D, L, R
    prefix_sums = {
        'U': [0],
        'D': [0],
        'L': [0],
        'R': [0]
    }
    
    for char in s:
        for move in 'UDLR':
            prefix_sums[move].append(prefix_sums[move][-1] + (char == move))

    # Calculate the number of distinct points
    distinct_points = set()
    n = len(s)
    
    for i in range(n - k + 1):
        end = i + k
        x = prefix_sums['R'][end] - prefix_sums['L'][i]
        y = prefix_sums['U'][end] - prefix_sums['D'][i]
        distinct_points.add((x, y))
    
    return len(distinct_points)