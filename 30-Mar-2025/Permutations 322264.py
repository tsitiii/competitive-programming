# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def backtrack(path, arr):
            if not arr:
                res.append(path)
                return
            for i in range(len(arr)):
                backtrack(path + [arr[i]], arr[:i] + arr[i+1:])
        
        backtrack([], nums)
        return res