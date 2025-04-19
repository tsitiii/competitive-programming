# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        matrix = [[-1]*col for _ in range(row)]  
        visited = [[False]*col for _ in range(row)]
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        que = deque()

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    que.append([i, j])
                    matrix[i][j] = 0  
                    visited[i][j] = True
        while que:
            i, j = que.popleft()
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and not visited[ni][nj]:
                    matrix[ni][nj] = matrix[i][j] + 1
                    visited[ni][nj] = True
                    que.append([ni, nj])

        return matrix
