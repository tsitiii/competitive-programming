# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp( target):
            if  target < 0:
                return 0
            if target == 0:
                return 1
            total = 0
            if target not in memo:
                for num in nums:
                    if num <= target:
                        total += dp(target-num)
                memo[target] = total
            return  memo[target]
        return  dp( target) 