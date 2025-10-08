# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(indx, i):
            if indx >= len(triangle):
                return 0
            state = (indx, i)
            if state not in memo:
                ans1 = triangle[indx][i] + dp(indx+1,i)
                ans2 = triangle[indx][i+1] + dp(indx+1, i+1)
                memo[state] = min(ans1 , ans2)
            return memo[state]
        return triangle[0][0] + dp(1,0)