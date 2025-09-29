# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, n): 
            for j in range(n): 
                up_val = dp[i-1][j]
                up_left_val = float('inf')
                if j > 0:
                    up_left_val = dp[i-1][j-1]
                up_right_val = float('inf') 
                if j < n - 1:
                    up_right_val = dp[i-1][j+1]
                
                dp[i][j] = matrix[i][j] + min(up_val, up_left_val, up_right_val)
        return min(dp[n-1])