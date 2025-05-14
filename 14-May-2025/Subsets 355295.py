# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 1 << n
        ans = []
        for i in range(m):
            res = []
            for j in range(n):
                if ((1 <<j) & i):
                    res.append(nums[j])
            ans.append(res)
        return ans