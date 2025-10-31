# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_position(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col
        
        visited = set()
        queue = collections.deque()
        queue.append((1, 0))
        visited.add(1)
        
        while queue:
            square, moves = queue.popleft()
            
            if square == n * n:
                return moves
            
            for next_square in range(square + 1, min(square + 6, n * n) + 1):
                r, c = get_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1