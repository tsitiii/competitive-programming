# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(indx, amount):
            if indx >= len(coins) or amount < 0:
                return 0
            if amount == 0:
                return 1
            state = (indx, amount)
            if state not in memo:
                include = 0
                exclude = dp(indx + 1, amount)
                if coins[indx] <= amount:
                    include = dp(indx, amount - coins[indx])
                memo[state] = include + exclude  
            return memo[state]
        return dp(0, amount)

