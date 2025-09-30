# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        dp = [[False]*(m+1) for _ in range((n+1))]

        for j in range(m + 1):
            dp[n][j] = True

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] =  dp[i+1][j+1]
                else:
                    dp[i][j] =  dp[i][j+1]
        return dp[0][0]