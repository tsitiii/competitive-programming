# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return   
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(board), len(board[0])
        
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        # def bfs(r, c):
        #     visited.add((r, c))
        #     que = deque([(r, c)])
            
        #     while que:
        #         rw, cl = que.popleft()
        #         for dr, dc in directions:
        #             tmpr, tmpc = rw + dr, cl + dc
        #             if (inbound(tmpr, tmpc) and 
        #                 (tmpr, tmpc) not in visited and 
        #                 board[tmpr][tmpc] == 'O'):
        #                 visited.add((tmpr, tmpc))
        #                 que.append((tmpr, tmpc))

        # def dfs(r,c):
        #     visited.add((r,c))
        #     for dr, dc in directions:
        #         tmpr, tmpc = dr+r, dc +c
        #         if inbound(tmpr, tmpc) and (tmpr, tmpc) not in visited and board[tmpr][tmpc] == 'O':
        #             visited.add((tmpr, tmpc))
        #             dfs(tmpr, tmpc)

        def bfs(r, c):
            visited.add((r,c))
            que = deque([(r,c)])
            while que: 
                rw, cl = que.popleft()
                for dr, dc in directions:
                    tmpr , tmpc = dr + rw, dc + cl
                    if inbound(tmpr, tmpc) and (tmpr, tmpc) not in visited and board[tmpr][tmpc] == 'O':
                        visited.add((tmpr, tmpc))
                        que.append((tmpr, tmpc))
        for i in range(row):
            for j in range(col):
                if(i == 0 or i == row-1 or j == 0 or j == col-1) and board[i][j] == 'O':
                    bfs(i,j)
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'