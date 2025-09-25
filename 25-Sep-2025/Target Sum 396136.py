# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} 
        def dp(indx, val):
            if indx >= len(nums) and val != target:
                return 0
            if indx == len(nums) and val == target:
                return 1

            state = (indx, val)
            if state not in memo:
                add = dp(indx + 1, val + nums[indx])
                sub = dp(indx + 1, val - nums[indx])
                memo[state] = add + sub
            return memo[state]
        return dp(0, 0)

