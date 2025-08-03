from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.min_id = list(range(size))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.min_id[root_u] = min(self.min_id[root_u], self.min_id[root_v])
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.min_id[root_v] = min(self.min_id[root_u], self.min_id[root_v])
            else:
                self.parent[root_v] = root_u
                self.min_id[root_u] = min(self.min_id[root_u], self.min_id[root_v])
                self.rank[root_u] += 1

    def get_min_id(self, u):
        return self.min_id[self.find(u)]

def solve(c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
    uf = UnionFind(c + 1)
    for u, v in connections:
        uf.union(u, v)

    online = [True] * (c + 1)
    result = []

    for query_type, x in queries:
        if query_type == 1:
            if online[x]:
                result.append(x)
            else:
                root_min_id = uf.get_min_id(x)
                result.append(root_min_id if online[root_min_id] else -1)
        elif query_type == 2:
            online[x] = False

    return result