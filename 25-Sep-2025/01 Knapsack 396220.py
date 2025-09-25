# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        memo = {}
        def dp(indx , W):
            if indx >= len(wt) or W <= 0:
                return 0
            state = (indx, W)
            if state not in memo:
                exclude = dp(indx + 1, W)
                include = 0
                if wt[indx] <= W:
                    include = val[indx] + dp(indx + 1, W- wt[indx])
                memo[state] = max(include, exclude)
            return memo[state]
        return dp(0, W)
