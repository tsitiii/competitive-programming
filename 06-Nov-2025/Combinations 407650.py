# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(node, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for nx in range(node, n + 1):
                path.append(nx)
                backtrack(nx + 1, path)
                path.pop()
        backtrack(1, [])
        return ans
            
            