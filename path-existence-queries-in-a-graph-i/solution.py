from typing import List

def solve(n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    def find_connected_components() -> List[int]:
        components = [0] * n
        current_component = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                components[i] = components[i - 1]
            else:
                current_component += 1
                components[i] = current_component
        return components

    def are_connected(u: int, v: int) -> bool:
        return components[u] == components[v]

    components = find_connected_components()
    result = [are_connected(u, v) for u, v in queries]
    return result