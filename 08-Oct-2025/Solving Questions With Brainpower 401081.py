# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(indx):
            if indx >= len(questions):
                return 0
            if indx not in memo:
                leave = dp(indx + 1)
                take = 0
                if indx + questions[indx][1] < len(questions):
                    take = questions[indx][0]+ dp(indx + questions[indx][1] + 1)
                else:
                    take = questions[indx][0]
                memo[indx] = max(take, leave)
            return memo[indx]
        return dp(0)