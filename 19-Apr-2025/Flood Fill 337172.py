# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        visited = [[False]*col for _ in range(row)]
        direction = [ (-1,0), (0, -1), (1,0), (0, 1) ]
        def inbound(i ,j):
            return 0<= i< row and 0<= j < col
        que = deque([(sr, sc)])
        start_pixel = image[sr][sc]
        while que:
            i, j = que.popleft() 
            image[i][j] = color
            visited[i][j] = True
            for left, right in direction:
                tempr = i + left
                tempc = j + right
                if inbound(tempr, tempc) and not visited[tempr][tempc] and image[tempr][tempc] == start_pixel:
                    que.append([tempr, tempc])
                    visited[tempr][tempc] = True
                    image[tempr][tempc] = color
        for i in range(row):
            for j in range(col):
                if image[i][j] == 0 and not visited[i][j]:
                    image[i][j] = 0
                    return image
        return image