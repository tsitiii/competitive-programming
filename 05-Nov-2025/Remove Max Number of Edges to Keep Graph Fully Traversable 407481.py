# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if xroot == yroot:
            return False
        
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        
        self.components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_dsu = DSU(n)
        bob_dsu = DSU(n)
        edges_used = 0
        for edge in edges:
            if edge[0] == 3:
                alice_union = alice_dsu.union(edge[1], edge[2])
                bob_union = bob_dsu.union(edge[1], edge[2])
                if alice_union or bob_union:
                    edges_used += 1
        for edge in edges:
            if edge[0] == 1:
                if alice_dsu.union(edge[1], edge[2]):
                    edges_used += 1
        for edge in edges:
            if edge[0] == 2:
                if bob_dsu.union(edge[1], edge[2]):
                    edges_used += 1
        if alice_dsu.components != 1 or bob_dsu.components != 1:
            return -1
        
        return len(edges) - edges_used