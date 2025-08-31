def solve(nums: list[int], swaps: list[list[int]]) -> int:
    # Union-Find data structure to manage connected components
    parent = list(range(len(nums)))

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> None:
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    # Union all indices that can be swapped
    for p, q in swaps:
        union(p, q)

    # Group elements by their connected component root
    from collections import defaultdict
    groups = defaultdict(list)
    for i, num in enumerate(nums):
        groups[find(i)].append(num)

    # Calculate the maximum alternating sum for each group
    max_alternating_sum = 0
    for group in groups.values():
        group.sort(reverse=True)
        # Add all odd-indexed elements (1-based) and subtract even-indexed elements
        max_alternating_sum += sum(group[i] for i in range(0, len(group), 2))
        if len(group) > 1:
            max_alternating_sum -= sum(group[i] for i in range(1, len(group), 2))

    return max_alternating_sum