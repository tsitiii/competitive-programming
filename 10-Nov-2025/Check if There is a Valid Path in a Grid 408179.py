# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        streets = {
            1: [False, True, False, True],
            2: [True, False, True, False], 
            3: [False, False, True, True],
            4: [False, True, True, False],
            5: [True, False, False, True],
            6: [True, True, False, False]
        }
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        visited = [[False] * n for _ in range(m)]
        stack = [(0, 0)]
        visited[0][0] = True
        
        while stack:
            x, y = stack.pop()
            if x == m - 1 and y == n - 1:
                return True
            
            street = grid[x][y]
            for direction in range(4):
                if streets[street][direction]:
                    dx, dy = dirs[direction]
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        neighbor_street = grid[nx][ny]
                        opposite_dir = (direction + 2) % 4
                        if streets[neighbor_street][opposite_dir]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
        
        return False