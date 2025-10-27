# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        edgeList.sort(key=lambda x: x[2])
        sorted_queries = sorted([(limit, u, v, i) for i, (u, v, limit) in enumerate(queries)])
        
        uf = UnionFind(n)
        answer = [False] * len(queries)
        
        edge_idx = 0
        for limit, u, v, orig_idx in sorted_queries:
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                uf.union(edgeList[edge_idx][0], edgeList[edge_idx][1])
                edge_idx += 1
            answer[orig_idx] = (uf.find(u) == uf.find(v))
        
        return answer