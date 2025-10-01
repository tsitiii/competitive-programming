# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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
                    sell = dp(indx + 1, not buying) + prices[indx] - fee
                    cooldown = dp(indx + 1, buying)
                    memo[state] = max(sell, cooldown)
            return memo[state]
        return dp(0, True)