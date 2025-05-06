# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n= len(edges)
        parent = [i for i in range(n+1)]
        size = [1] * (n+1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        ans = []
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
               return True
               
            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
            return False
            
        for i, j in edges:
            if  union(i,j):
                return [i, j]
        

            
                