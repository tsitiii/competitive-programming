# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [poured]
        
        for row in range(1, query_row + 1):
            next_row = [0.0] * (row + 1)
            for col in range(len(current_row)):
                excess = current_row[col] - 1
                if excess > 0:
                    next_row[col] += excess / 2.0
                    next_row[col + 1] += excess / 2.0
            
            current_row = next_row
        
        return min(1.0, current_row[query_glass])