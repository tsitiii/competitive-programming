# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        matrix = [[-1]*col for _ in range(row)]
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        que = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    matrix[i][j] = 0
                    que.append((i, j))

        while que:
            i, j = que.popleft()
            for dx, dy in direction:
                ni, nj = i + dx, j + dy
                if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == -1:
                    matrix[ni][nj] = matrix[i][j] + 1
                    que.append((ni, nj))
        return matrix