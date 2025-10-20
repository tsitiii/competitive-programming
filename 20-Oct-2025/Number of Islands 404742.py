# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        island = 0
        directions = [[0,1], [1,0], [-1, 0], [0, -1]]
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        def bfs(r ,c):
            que = deque([(r,c)])
            visited.add((r,c))
            while que:
                rw, co = que.popleft()
                for dr, dc in directions:
                    tempr, tempc = dr + rw, dc + co
                    if inbound(tempr, tempc) and (tempr, tempc) not in visited and grid[tempr][tempc] =='1':
                        visited.add((tempr, tempc))
                        que.append([tempr, tempc])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i, j)
                    island += 1
        return island