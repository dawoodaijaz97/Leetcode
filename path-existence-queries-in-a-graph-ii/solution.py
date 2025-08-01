from collections import defaultdict, deque
from typing import List

def solve(n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
    # Build the graph
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(nums[i] - nums[j]) <= maxDiff:
                graph[i].append(j)
                graph[j].append(i)

    def bfs(start: int, end: int) -> int:
        if start == end:
            return 0
        queue = deque([(start, 0)])
        visited = set([start])
        while queue:
            node, dist = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == end:
                    return dist + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return -1

    # Process each query
    result = []
    for u, v in queries:
        result.append(bfs(u, v))

    return result