# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        diff = abs(startPos - endPos)
        if diff > k or (k - diff) % 2 != 0:
            return 0
        right_steps = (k + diff) // 2
        left_steps = (k - diff) // 2
        dp = [[0] * (k + 1) for _ in range(k + 1)]
        
        for i in range(k + 1):
            dp[i][0] = 1
            dp[i][i] = 1
        
        for i in range(1, k + 1):
            for j in range(1, i):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
        
        return dp[k][right_steps]