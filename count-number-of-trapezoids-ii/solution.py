from typing import List, Tuple

def solve(points: List[List[int]]) -> int:
    def slope(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
        if p1[0] == p2[0]:
            return float('inf')
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def is_trapezoid(p1, p2, p3, p4):
        s1 = slope(p1, p2)
        s2 = slope(p3, p4)
        s3 = slope(p1, p3)
        s4 = slope(p2, p4)
        return (s1 == s2) or (s3 == s4)

    n = len(points)
    trapezoid_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if is_trapezoid(tuple(points[i]), tuple(points[j]), tuple(points[k]), tuple(points[l])):
                        trapezoid_count += 1

    return trapezoid_count