# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.count -= 1
        return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self.areSimilar(strs[i], strs[j]):
                    uf.union(i, j)
        
        return uf.count
    
    def areSimilar(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff_positions = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_positions.append(i)
        if len(diff_positions) != 2:
            return False
        i, j = diff_positions
        return s1[i] == s2[j] and s1[j] == s2[i]