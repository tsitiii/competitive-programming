# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False]*col for _ in range(row)] 
        directions = [ (-1, 0),  (1,0), (0, 1), (0, -1) ]
        total = 0
        def inbound(i,j):
            return 0 <= i < row and 0 <= j < col
        def dfs(row, col):
            nonlocal cnt
            cnt +=1 
            for left, right in directions:
                tempr  = row + left
                tempc = col + right
                if inbound(tempr, tempc) and grid[tempr][tempc] == 1 and not visited[tempr][tempc]:
                    visited[tempr][tempc] = True
                    dfs(tempr, tempc)

        for i in range(row):
            for j in range(col):
                cnt =0
                if grid[i][j] ==1 and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j)
                    total = max(total,cnt)
        return total