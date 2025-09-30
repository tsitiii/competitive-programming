# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(indx):
            if indx >= len(cost):
                return 0
            if indx not in memo:
                one_step = cost[indx] + dp(indx+1)
                two_step = cost[indx] + dp(indx +2)
                memo[indx] = min(one_step , two_step)
            return memo[indx]
        return min(dp(0), dp(1))