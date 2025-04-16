# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False]*col for _ in range(row)]
        def inbound(i ,j):
            return 0<= i< row and 0<= j < col
        direction = [ (-1,0),(0, -1), (1,0), (0, 1) ]
        que = deque()
        cnt = -1
        for i in range(row):
            for j in range(col):
                an = 0
                if not visited[i][j] and grid[i][j] == 2:
                    que.append([i, j])  
                    visited[i][j] = True
        cost = 0
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()

                for r , c in direction:
                    tempr = r + i
                    tempc = c + j
                    if inbound(tempr, tempc) and not visited[tempr][tempc] and grid[tempr][tempc] == 1:
                            que.append([tempr, tempc])
                            visited[tempr][tempc] = True
            cost += 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1 
        if cost == 0:
            return 0
        return cost -1
    




