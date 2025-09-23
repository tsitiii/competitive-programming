# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        res = 1
        def dp(indx):
            if indx >= len(nums):
                return 0
            if indx not in memo:
                memo[indx] = 1
                for j in range(indx + 1, len(nums)):
                   if nums[j] > nums[indx]: 
                        memo[indx] = max(memo[indx],1 + dp(j))
            return memo[indx]
        for i in range(len(nums)):
            res = max(dp(i),res)
        return res