# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def dp(indx: int, amount: int) -> int:
            if amount == 0:
                return 0 
            if indx >= n or amount < 0:
                return float('inf') 
            state = (indx, amount)
            if state not in memo:
                exclude = dp(indx + 1, amount)
                include = float('inf')
                if coins[indx] <= amount:
                    curr_include = dp(indx, amount - coins[indx])
                    if curr_include != float('inf'):
                        include = 1 + curr_include
                memo[state] = min(include, exclude)
            return memo[state]
        
        res = dp(0, amount)
        return res if res != float('inf') else -1