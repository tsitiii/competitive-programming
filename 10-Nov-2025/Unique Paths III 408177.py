# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_x = start_y = 0
        empty_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                if grid[i][j] == 0:
                    empty_count += 1
        total_to_visit = empty_count + 1
        
        def dfs(x, y, visited_count):
            if grid[x][y] == 2:
                return 1 if visited_count == total_to_visit else 0
            temp = grid[x][y]
            grid[x][y] = -1
            
            paths = 0
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    paths += dfs(nx, ny, visited_count + 1)
            grid[x][y] = temp
            return paths
        
        return dfs(start_x, start_y, 0)