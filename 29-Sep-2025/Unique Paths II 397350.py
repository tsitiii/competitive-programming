# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0 
        dp[0][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 0 and dp[0][j-1] > 0:
                dp[0][j] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] > 0:
                dp[i][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
