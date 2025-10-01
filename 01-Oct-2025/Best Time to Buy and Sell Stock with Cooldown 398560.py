# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(indx, buying):
            if indx >= len(prices):
                return 0
            state = (indx, buying) 
            if state not in memo:
                if buying :
                    buy = dp(indx + 1, not buying) - prices[indx]
                    cooldown = dp(indx + 1, buying)
                    memo[state] = max(buy, cooldown)
                else:
                    sell = dp(indx + 2, not buying) + prices[indx]
                    cooldown = dp(indx + 1 , buying)
                    memo[state] = max(sell, cooldown)
            return memo[state]
        return dp(0, True)