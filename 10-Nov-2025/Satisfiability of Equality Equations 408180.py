# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        for eq in equations:
            if eq[1] == '=':
                a, b = eq[0], eq[3]
                union(a, b)
        for eq in equations:
            if eq[1] == '!':
                a, b = eq[0], eq[3]
                if find(a) == find(b):
                    return False  
        return True